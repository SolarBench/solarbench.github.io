# SolarBench website

This repository contains the Jekyll source for the SolarBench research website. As a project repository under the `Solar4cast` GitHub organization, its GitHub Pages URL is `https://solar4cast.github.io/solarbench-site/`. The URL `https://solarbench.github.io/` belongs to the separate `SolarBench` organization and cannot be served from this repository.

## Preview locally

Install the dependencies with `bundle install`, then run:

```bash
bundle exec jekyll serve --baseurl ""
```

Open `http://127.0.0.1:4000/`. To test the published path, run `bundle exec jekyll build` and inspect `_site`; the configured `baseurl` is `/solarbench-site`.

## Publish

In the repository's **Settings → Pages**, set **Build and deployment → Source** to **GitHub Actions**. The workflow in `.github/workflows/pages.yml` builds and deploys on pushes to `main`. Check that the repository visibility and all public-facing content are ready before pushing release changes.

For future contributions, make changes on a branch and open a pull request to `main` so they can be reviewed and checked before deployment. The maintainer may continue working directly on `main` while developing the initial site.

The interactive map uses Leaflet and locally hosted Natural Earth geography, solar-radiation imagery, and climate imagery. Each site links to Google Maps for optional satellite inspection. The public website does not use a Mapbox token or Mapbox services.
