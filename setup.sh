mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"tooba.se16@iba-suk.edu.pk\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml