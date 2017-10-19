echo "Uploading to Heroku"
sudo heroku container:login
sudo heroku container:push web --app $HEROKU_APP_NAME
echo "Uploaded to Heroku"