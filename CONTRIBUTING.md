# Contributing

The instructions below are written assuming you're using VS Code because Home Assistant appears to assume that too.

## First time setup

1. Clone the repo
1. Open this repo in a devcontainer
1. Use VS Code's **Run Task** functionality to `Start Home Assistant`
   You should get a notification that port 80 has been forwarded.
1. In the pane at the bottom, click on Ports.
1. Find the row where Port is 80.
1. Click the globe icon in the Forwarded Address column to open Home Assistant.
   Complete the initial setup.
1. Use VS Code's **Run Task** functionality to `Install App`
   You should see "Command completed successfully." twice.
1. Navigate to **Apps** > **Donetick Addon (dev)** > **Configuration**
1. Set the jwt_secret to a random 32-character string
1. Use VS Code's **Run Task** functionality to `Start App`
   You should see port 2021 available now.

## Making changes

1. Make your changes
1. Use VS Code's **Run Task** functionality to `Rebuild and Start App`

## Important Note

Only `Install App` and `Rebuild and Start App` sync the real directory (`donetick`) to the folder that gets read in by the Home Assistant supervisor (donetick_dev)
This is because:

- the slug in `donetick/config.yaml` is set to `Donetick` instead of all lowercase
- Home Assistant uses the slug to determine the docker image name
- docker image names must be lowercase
