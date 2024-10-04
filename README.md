Welcome to my open source project for soccer (football) player tracking! The motivation behind this project is to make a tracking solution that works on football broadcast video and is TRULY open source.

This project is largely based off of [this Roboflow YouTube video](https://www.youtube.com/watch?v=aBVGKoNZQUw).

# Data
I got my training data from the following locations:
- [Player and ball dataset](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc) (version 12)
- [Pitch keypoint dataset](https://universe.roboflow.com/roboflow-jvuqo/football-field-detection-f07vi) (version 15)
- [Bundesliga Data Shootout data](https://www.kaggle.com/datasets/saberghaderi/-dfl-bundesliga-460-mp4-videos-in-30sec-csv?resource=download-directory) (used this as input videos to test models)

To download the Roboflow data for yourself:
1. Click "Download Project".
2. Select the dataset version you want. The versions I used are listed above.
3. Click "Download Dataset".
4. Choose "YOLOv8" for the format.
5. Select "Download zip to computer".
6. Click "Continue". The dataset ZIP will download.
7. When the download is complete, unzip the data. The unzipped folder should contain `test`, `train`, and `valid` folders as well as `data.yaml` and a couple of READMEs.
8. Move the unzipped folder to the appropriate `datasets` folder. either under `player_and_ball_detection_model` or `keypoint_detection_model`.

