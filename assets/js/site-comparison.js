(() => {
  const dataNode = document.getElementById('comparison-data');
  if (!dataNode) return;
  const sites = JSON.parse(dataNode.textContent);
  const feature = document.getElementById('comparison-feature');
  const order = document.getElementById('comparison-order');
  const category = document.getElementById('comparison-sample-category');
  const chart = document.getElementById('comparison-chart');
  const day = 86400000;
  const start = site => Date.parse(site.start_date + 'T00:00:00Z');
  const end = site => Date.parse(site.end_date + 'T00:00:00Z');
  const metrics = {
    radiation: {value: s => s.solar_radiation?.mean_w_m2, format: v => v.toFixed(1) + ' W/m²', note: 'ERA5 · Long-term mean, 1980–2020. Bars start at zero.'},
    variability: {value: s => s.variability?.index, format: v => v.toFixed(3), note: 'Root mean square of consecutive 5-min changes in the clear sky index; higher values indicate greater short-term variability.'},
    ramps: {value: s => s.variability?.large_ramp_fraction, format: v => (v * 100).toFixed(1) + '%', note: 'Proportion of consecutive 5-min intervals with an absolute change in clear sky index exceeding 0.1.'},
    span: {value: s => (end(s) - start(s)) / day, format: v => (v / 365.25).toFixed(1) + ' years', note: 'Observation periods on a shared calendar axis. Spans do not imply continuous coverage and data may contain interruptions.'},
    samples: {value: s => s.sample_counts?.[category.value], format: v => v.toLocaleString('en-US'), note: 'Sample counts are compared within the selected data category. Missing counts are not treated as zero.'}
  };
  function element(tag, cls, text) {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function render() {
    const key = feature.value;
    const metric = metrics[key];
    document.getElementById('comparison-sample-control').hidden = key !== 'samples';
    const description = document.getElementById('comparison-description');
    description.hidden = key !== 'span';
    description.textContent = key === 'span' ? metric.note : '';
    const rows = sites.map(site => ({site, value: metric.value(site)}));
    rows.sort((a, b) => {
      if (order.value !== 'name') {
        const aMissing = !Number.isFinite(a.value), bMissing = !Number.isFinite(b.value);
        if (aMissing !== bMissing) return aMissing ? 1 : -1;
        if (!aMissing && a.value !== b.value) return (a.value - b.value) * (order.value === 'descending' ? -1 : 1);
      }
      return a.site.site_name.localeCompare(b.site.site_name, 'en');
    });
    const max = Math.max(0, ...rows.map(row => Number.isFinite(row.value) ? row.value : 0)) || 1;
    const firstYear = new Date(Math.min(...sites.map(start))).getUTCFullYear();
    const lastYear = new Date(Math.max(...sites.map(end))).getUTCFullYear();
    const minDate = Date.UTC(firstYear, 0, 1), maxDate = Date.UTC(lastYear + 1, 0, 1);
    const ticks = [];
    for (let year = firstYear; year <= lastYear; year++) {
      for (let quarter = 0; quarter < 4; quarter++) {
        ticks.push({year, quarter, position: (Date.UTC(year, quarter * 3, 1) - minDate) / (maxDate - minDate) * 100});
      }
    }
    chart.className = key === 'span' ? 'comparison-timeline' : 'comparison-numeric';
    chart.replaceChildren();
    if (key === 'span') {
      const axis = element('div', 'comparison-axis');
      for (const tick of ticks) {
        const mark = element('span', 'comparison-tick' + (tick.quarter === 0 ? ' year-tick' : ''));
        mark.style.left = tick.position + '%';
        if (tick.quarter === 0) mark.append(element('span', '', String(tick.year)));
        axis.append(mark);
      }
      chart.append(axis);
    }
    const list = element('ul', 'comparison-rows');
    for (const {site, value} of rows) {
      const row = element('li', 'comparison-row');
      row.append(element('span', 'comparison-name', site.site_name));
      const track = element('div', 'comparison-track');
      track.setAttribute('aria-hidden', 'true');
      if (key === 'span') for (const tick of ticks) {
        const grid = element('span', 'comparison-gridline' + (tick.quarter === 0 ? ' year-gridline' : ''));
        grid.style.left = tick.position + '%';
        track.append(grid);
      }
      if (Number.isFinite(value)) {
        const bar = element('span', 'comparison-bar');
        bar.style.width = (key === 'span' ? (end(site) - start(site)) / (maxDate - minDate) : value / max) * 100 + '%';
        if (key === 'span') {
          bar.style.marginLeft = (start(site) - minDate) / (maxDate - minDate) * 100 + '%';
          bar.title = site.start_date + ' – ' + site.end_date;
        }
        track.append(bar);
      }
      row.append(track);
      const missing = key === 'samples' && category.value === 'satellite' && !site.data.includes('Satellite imagery') ? 'Not available' : 'Not yet provided';
      const label = element('span', 'comparison-value', Number.isFinite(value) ? metric.format(value) : missing);
      if (key === 'span') label.title = site.start_date + ' – ' + site.end_date;
      row.append(label);
      list.append(row);
    }
    chart.append(list);
  }
  [feature, order, category].forEach(control => control.addEventListener('change', render));
  render();
})();
