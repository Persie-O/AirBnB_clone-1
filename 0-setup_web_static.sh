#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Check if running with root privileges
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run with root privileges." >&2
    exit 1
fi

# Install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
    echo "Installing Nginx..."
    apt-get update
    apt-get -y install nginx
fi

web_static_dir="/data/web_static"
current_link="$web_static_dir/current"

# Create necessary directories if they don't exist
mkdir -p "$web_static_dir/releases/test"
mkdir -p "$web_static_dir/shared"

# Create a test HTML file
echo "<html>
    <head>
    </head>
    <body>
        <h1>Holberton School</h1>
    </body>
</html>" > "$web_static_dir/releases/test/index.html"

# Create a symbolic link
if [ -L "$current_link" ]; then
    rm "$current_link"
fi
ln -s "$web_static_dir/releases/test" "$current_link"

# Set ownership of the /data/ folder recursively
chown -R ubuntu:ubuntu "$web_static_dir"

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
nginx_config="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$hostname;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias $web_static_dir/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://github.com/Persie-O;
    }
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}"

if ! grep -q "location /hbnb_static" "$config_file"; then
    printf "%s" "$nginx_config" > "$config_file"
    nginx -t
    service nginx restart
fi

exit 0
