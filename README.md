# SeeMyFeels
Audio to Generative Art. IC Hello World 2021 Project entry.

Ever really been into a song? Stuck in your feels and want a way to remember that track? Make it memorable, with a unique piece of art that represents that sound.

## Sources
- [Essentia](https://essentia.upf.edu/)
- [Generative Art](https://github.com/JakobGlock/Generative-Art)

## Progress
We started by playing around with different parameters and some of the existing art styles in the Generative-Art repo, figuring out what changes caused what effects in the outputted image. Here are some first examples:

![Large circles](https://github.com/shnupta/SeeMyFeels/blob/main/doc-images/big-circles.png?raw=true)
![Small circles](https://github.com/shnupta/SeeMyFeels/blob/main/doc-images/small-circles.png?raw=true)
![Wavey](https://github.com/shnupta/SeeMyFeels/blob/main/doc-images/waves.png?raw=true)

## Development Tips
To save rebuilding or pulling the docker image, you can mount your working directory when running `docker run`. You can do this by:

```
docker run --mount type=bind,source=<ABSOLUTE_SOURCE>,target=/smf shnupta/seemyfeels
```
