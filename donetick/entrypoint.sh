#!/usr/bin/with-contenv bashio


# Envirment variables:
export DT_TELEGRAM_TOKEN=$(bashio::config 'telegram_token')
export DT_PUSHOVER_TOKEN=$(bashio::config 'pushover_token')
export DT_DISABLE_SIGNUP=$(bashio::config 'disable_signup')


export DT_OAUTH2_CLIENT_ID=$(bashio::config 'oauth2_client_id')
export DT_OAUTH2_CLIENT_SECRET=$(bashio::config 'oauth2_client_secret')
export DT_OAUTH2_REDIRECT_URI=$(bashio::config 'oauth2_redirect_uri')
export DT_OAUTH2_AUTH_URL=$(bashio::config 'oauth2_auth_url')
export DT_OAUTH2_TOKEN_URL=$(bashio::config 'oauth2_token_url')
export DT_OAUTH2_USER_INFO_URL=$(bashio::config 'oauth2_user_info_url')
export DT_OAUTH2_NAME=$(bashio::config 'oauth2_name')

# Start donetick backend and save PID 
bashio::log.info "Starting Donetick backend..."

# Envirment variables:
# export VITE_APP_API_URL=http://host.docker.internal:2021

cd /app/core
# Start donetick backend and save PID 
export DT_ENV="selfhosted"

ls -lR /app/
./donetick &
PID1=$!




cleanup() {
    echo "Terminating processes..."
    kill $PID1 
}

# Trap SIGINT & SIGTERM to clean up before exiting
trap cleanup SIGINT SIGTERM

# Wait for both processes to exit
wait $PID1  

echo "Both processes have completed."
