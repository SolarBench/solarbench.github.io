# SolarBench website

This repository contains the Jekyll source for the SolarBench research website, configured for `https://solarbench.github.io/` with an empty `baseurl`. The repository must be named `SolarBench.github.io` under the `SolarBench` GitHub organization to serve this URL.

## Preview locally

Install the dependencies with `bundle install`, then run:

```bash
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000/`. To test the published site, run `bundle exec jekyll build` and inspect `_site`.

## Publish

In the repository's **Settings → Pages**, set **Build and deployment → Source** to **GitHub Actions**. The workflow in `.github/workflows/pages.yml` builds and deploys on pushes to `main`. Check that the repository visibility and all public-facing content are ready before pushing release changes.

For future contributions, make changes on a branch and open a pull request to `main` so they can be reviewed and checked before deployment.
