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

### Storage settings

S3-compatible storage remains the recommended production provider. It can be
hosted by another provider or run on your own network: self-hosting does not
require AWS or sending photos to a cloud service. A separate storage project
manages the files and persistence; DoneTick connects through its S3 API.

The default `storage_type: auto` preserves existing backend configuration.
It does not select local storage or provision a bucket. With no storage configured,
DoneTick still starts, but uploads require storage setup and may return an error.
Disabling upload controls and showing setup guidance requires a separate backend
and frontend change; this add-on configuration does not implement that behavior.

Change settings in the app's **Configuration** tab, save, and restart the app.
Storage fields other than `storage_type` are optional and have no add-on defaults.
Omitted or blank fields preserve backend YAML/environment settings. Nonempty fields
override them, including `storage_path_style: false`. Remove the path-style option
from the configuration YAML to restore its backend value. To clear an existing
backend S3 prefix or endpoint, change that backend setting at its source.
`storage_type: auto` preserves the provider but still applies other supplied fields.

| Option | Default | Explanation |
|--------|---------|-------------|
| `storage_type` | `auto` | Preserve backend provider; `s3` explicitly selects S3; `local` explicitly selects development filesystem storage. |
| `storage_base_path` | omitted | S3 object prefix or local directory. Blank preserves the S3 prefix; explicitly selecting local defaults to `/data/uploads`. |
| `storage_bucket_name` | omitted | S3 bucket name. |
| `storage_region` | omitted | Region required by the storage provider. |
| `storage_access_key` | omitted | S3 access key. |
| `storage_secret_key` | omitted | S3 secret key. |
| `storage_endpoint` | omitted | S3-compatible endpoint; blank preserves the backend endpoint (AWS S3 by default). |
| `storage_path_style` | omitted | Enable for services requiring path-style addressing. Requires a backend version supporting `storage.path_style`. |

#### Keep production storage on your own network

Run an S3-compatible service separately on your server or NAS, create a bucket and
credentials, then configure DoneTick, for example:

```yaml
storage_type: s3
storage_bucket_name: donetick
storage_region: us-east-1
storage_access_key: YOUR_ACCESS_KEY
storage_secret_key: YOUR_SECRET_KEY
storage_endpoint: https://storage.home.example
storage_base_path: assets
storage_path_style: true
```

Use the region and addressing mode required by your service. The endpoint must be
reachable from the add-on and from browsers/devices displaying photos because S3
asset URLs can point directly to that endpoint. Back up the bucket using the
storage service's tools. See the [backend storage guide](https://docs.donetick.com/advance-settings/storage-setup/).

#### Local filesystem storage (development / personal opt-in)

The backend already provides filesystem storage. To use it explicitly without
setting up an S3 service:

```yaml
storage_type: local
storage_base_path: /data/uploads
```

Selecting `local` resets the upload directory to `/data/uploads` unless a nonempty
`storage_base_path` option is supplied, so an inherited S3 prefix cannot become a
relative filesystem path. This keeps uploads in the app's persistent data directory across restarts and app
updates, and logs a warning at startup. Upstream recommends local storage only
for development; this option does not change that support policy or make it the
production default. Keep custom paths under `/data` and include uploads in backups
alongside the database. Persistence across updates is not a substitute for backups.

Changing providers, S3 prefixes, or local directories does not migrate existing
uploads or rewrite stored image references. Back up first and migrate separately.
Installations already using the earlier revision of this PR should explicitly
keep `storage_type: local` and `/data/uploads` to continue using their local files.
The same storage options are available in the beta app.

## Support
For issues, feature requests, or questions, please open an issue on the [GitHub repository](https://github.com/donetick/hassio-addons/issues).

## Changelog
See [CHANGELOG.md](CHANGELOG.md) for release notes and version history.

## License
This project is licensed under the terms of the [Apache License 2.0](../LICENSE).
