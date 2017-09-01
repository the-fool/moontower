# Set Up

The code was made with Hugo v0.26 -- make sure you're up to date.

Get [hugo](https://gohugo.io/getting-started/installing/).

(Hugo is a program that assembles a finished website from a kit we give it.  It's easier for us to make a kit with instructions rather than do all the meticulous low-level plumbing by hand.  This source code is a kit with instructions for Hugo.)


# First steps

## Clone the repo once in the beginning
In a shell, `cd` to a place where you want the code to be.  Then:
```bash
git clone https:github.com/the-fool/moontower
```


## Make changes and save changes
You only need to `clone` **once**.  From that point forward, when you want to update your code, you go to the root directory of the project and:
```bash
# 'pulls' in the most recent code and brings your own local copy up to date
git pull
```

Any time you are ready to make a change, do the following:

```bash
# collect all your changes into a 'staging area'
git add -A 

# save your changes with a helpful message explaining what you did
git commit -m "I changed XYZ because of PDQ"

# upload your changes to our shared GitHub server
git push
```

# Do

There is a swiss-army script for doing things.  Run the following commands in a shell at the root directory of the project.

## To serve in development mode
`./do serve`

This will run a server, that by default serves the app at `127.0.0.1:1313`.  Most changes you save to a file will automatically refresh the page.

## To build a final version of the site
`./do build`
This script 'builds' the final product into a bunch of files ready to ship.  You only 'build' the project when you are wanting to upload it to the actual server in the cloud.


# Changing things

There are 2 directories in the root that interest us: `layouts` and `static`.  The other directories can be pretty well ignored 99% of the time.

## ./static

The focus here is on the `.css` files.  They style the app.  There is a `main.css` which applies to every page.  And then each page has its own special styles (for example `faq.css`).

This directory is also where images go and icons go.


## ./layouts

This is the meat of the _content_ of the site.

The homepage is `layouts/index.html`, and each other page is in a directory with its name.  The FAQ page is at `layouts/faq/single.html`, and the About page is at `layouts/about/single.html` (the `single` is a naming convention for the Hugo program).

Now, each page is nested in some *common* content.  That common content is at `layouts/_default/baseof.html`.  The common stuff includes things like that top navbar, and fundamental changes to layout depending on whether we're viewing the site on a small screen.

But, the most important thing which we will change the most: `layouts/partials/`.  I broke up pieces of the content into 'partials'.  This makes it easier to find the things we want to change, and make the change.  The 'skeleton' of the page is a layout, like `layouts/about/single.html` -- but the actual **stuff** that's likely to change exists as separate parts. 

