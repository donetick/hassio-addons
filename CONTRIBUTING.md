# Contributing

The instructions below are written assuming you're using VS Code because Home Assistant appears to assume that too.

1. Clone the repo
1. Open this repo in a devcontainer
1. Use VS Code's "Run Task" functionality to start Home Assistant
1. Open http://localhost:7123 and go through the initial setup process
1. Comment out the `image` in config.yaml so the addon is built locally instead of using the precompiled docker image (make sure to not commit that change)
1. Use VS Code's "Run Task" functionality to start the addon; it will fail
1. Open DoneTick addon in the web interface and set the jwt_secret
1. Use VS Code's "Run Task" functionality to start the addon
1. Make your changes
1. Use VS Code's "Run Task" functionality to rebuild and start the addon
