@default:
    just --list

# Start Jekyll development server
up:
    jekyll serve --watch

# Build the Jekyll site
build:
    jekyll build
