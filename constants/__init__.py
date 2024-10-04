import os

PROJECT_ROOT = "/home/helen/Documents/GitHub/open_source_tracking"

# == Player and ball detection =====================================================================
PLAYER_BALL_DATASETS = os.path.join(PROJECT_ROOT, "player_and_ball_detection_model", "datasets")
PLAYER_BALL_DATASET_NAME = "football-players-detection.v12i.yolov8"

PLAYER_BALL_IMGSZ = 1280
PLAYER_BALL_BATCH = 1  # with 8 GB P4000, batch size = 1 takes about 4.4 GB

BALL_ID = 0
GK_ID = 1
PLAYER_ID = 2
REF_ID = 3

# == Pitch keypoint detection ======================================================================
KEYPOINT_DATASETS = os.path.join(PROJECT_ROOT, "keypoint_detection_model", "datasets")
KEYPOINT_DATASET_NAME = "football-field-detection.v15i.yolov8"

KEYPOINT_IMGSZ = 640
KEYPOINT_BATCH = 2
