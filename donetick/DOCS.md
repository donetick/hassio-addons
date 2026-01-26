# Home Assistant Add-on: DoneTick

## Installation

To install the addon, add this repository to your Home Assistant addon store and then install it.

To add the repo:

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FDonetick%2Fhassio-addons)

To install the add-on:

[![Open this add-on in your Home Assistant instance.](https://my.home-assistant.io/badges/supervisor_addon.svg)](https://my.home-assistant.io/redirect/supervisor_addon/?addon=2c57906a_Donetick)

Manual instructions:

1. Open Home Assistant in your web browser.
1. Go to Settings > Add-ons > Add-on Store.
1. Click the three-dot menu in the top-right corner and select Repositories.
1. Enter the URL of this repository: https://github.com/Donetick/hassio-addons
1. Click Add
1. Click Close
1. Search for DoneTick in the list of add-ons and click it.

## How To use

1. Start the add-on.
1. Open the Web UI.
1. Create the first user account

## Configuration
```
telegram_token: ""
pushover_token: ""
disable_signup: false
auth_provider: ""
oauth2_client_id: ""
oauth2_client_secret: ""
oauth2_redirect_url: ""
oauth2_auth_url: ""
oauth2_token_url: ""
oauth2_user_info_url: ""
oauth2_name: ""
jwt_secret: null
email_email: ""
email_key: ""
email_host: ""
email_port: 587
email_appHost: ""
```

### Core Settings

| Option                | Required | Default | Explanation
|-----------------------|----------|---------|------------------
| telegram_token        | no       |         | optional token for telegram integration
| pushover_token        | no       |         | optional token for pushover integration
| disable_signup        | no       | false   | If true, disables user signups.
| jwt_secret            | yes      |         | secret needed by donetick backend. Run `node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"` to generate and paste it in the field.

### OAuth2 Settings
Any OAuth2 provider that supports OIDC

| Option                | Required | Default | Explanation
|-----------------------|----------|---------|------------------
| auth_provider         | no       |         | `3rdPartyAuth`?
| oauth2_client_id      | no       |         | Client ID
| oauth2_client_secret  | no       |         | Client Secret
| oauth2_redirect_url   | no       |         | `https://{YOUR_URL}/auth/oauth2`
| oauth2_auth_url       | no       |         |
| oauth2_token_url      | no       |         |
| oauth2_user_info_url  | no       |         |
| oauth2_name           | no       |         |

### Email Settings
If you want DoneTick to be able to send emails make sure to configure the below settings.
NOTE - if `email_port` is not set, the server will not start.

| Option                | Required | Default | Explanation
|-----------------------|----------|---------|------------------
| email_email           | no       |         | The email address you use to authenticate to send emails via SMTP
| email_key             | no       |         | The API key used to authenticate to your email provider
| email_host            | no       |         | SMTP server address for your email provider
| email_port            | yes      | 587     | SMTP port for your email provider
| email_appHost         | no       |         | Your DoneTick instance's URL (incl. http(s) and port)

## Support
For issues, feature requests, or questions, please open an issue on the [GitHub repository](https://github.com/donetick/hassio-addons/issues).

## Changelog
See [CHANGELOG.md](CHANGELOG.md) for release notes and version history.

## License
This project is licensed under the terms of the [Apache License 2.0](../LICENSE).
