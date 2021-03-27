# SeeMyFeels
Audio to Generative Art. IC Hello World 2021 Project.

## Development Tips
To save rebuilding or pulling the docker image, you can mount your working directory when running `docker run`. You can do this by:

```
docker run --mount type=bind,source=<ABSOLUTE_SOURCE>,target=/smf shnupta/seemyfeels
```
