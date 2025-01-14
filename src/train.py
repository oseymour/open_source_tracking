import marimo

__generated_with = "0.10.12"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    import rootutils
    import os
    from ultralytics import YOLO, settings
    import os
    import yaml

    root = rootutils.find_root()

    with open(os.path.join(root, \"config.yaml\"), \"r\") as f:
        cfg = yaml.safe_load(f)

    model_to_train = cfg[\"model_to_train\"]
    project_dir = os.path.join(root, cfg[model_to_train][\"project_dir\"])
    datasets_dir = os.path.join(project_dir, \"datasets\")
    dataset = os.path.join(datasets_dir, cfg[model_to_train][\"dataset_name\"])

    Point ultralytics to the datasets for this specific training
    settings.update({
        \"datasets_dir\": datasets_dir,
    })

    # Shared args for the YOLO train() and val() calls later
    yolo_args = {
        \"data\": os.path.join(dataset, \"data.yaml\"),
        \"imgsz\": cfg[model_to_train][\"imgsz\"],
        \"batch\": cfg[model_to_train][\"batch_size\"],
        \"project\": project_dir,
    }
    """,
    name="_"
)


@app.cell
def _(YOLO, cfg, dataset, model_to_train, os, project_dir, yolo_args):
    # Clear label caches, if they exist
    for folder in ["train", "valid", "test"]:
        label_cache_path = os.path.join(dataset, folder, "labels.cache")
        if os.path.exists(label_cache_path):
            print(f"Deleting {label_cache_path}.")
            os.remove(label_cache_path)

    # Init the model
    model = YOLO(os.path.join(project_dir, cfg[model_to_train]["pretrained_weights"]))
    _ = model.info()

    # Train the model
    model.train(
        **yolo_args,
        epochs=cfg[model_to_train]["epochs"],
    )
    return folder, label_cache_path, model


@app.cell
def _(model, yolo_args):
    model.val(**yolo_args)
    return


if __name__ == "__main__":
    app.run()
