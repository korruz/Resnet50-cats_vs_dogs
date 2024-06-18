import csv
import os
from torchvision import transforms
from PIL import Image
from torch.utils.data import Dataset
from modelscope.msdatasets import MsDataset


class DatasetLoader(Dataset):
    # def __init__(self, csv_path):
    #     self.csv_file = csv_path
    #     with open(self.csv_file, "r") as file:
    #         self.data = list(csv.reader(file))

    #     self.current_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, model: str) -> None:
        assert model in ["train", "val"]
        if model == "train":
            self.data = MsDataset.load(
                "tany0699/cats_and_dogs", subset_name="default", split="train"
            )
        elif model == "val":
            self.data = MsDataset.load(
                "tany0699/cats_and_dogs", subset_name="default", split="validation"
            )
        else:
            raise ValueError("Invalid model type")

    def preprocess_image(self, image_path):
        """
        Preprocess the image: Read the image, apply transformations, and return the transformed image.
        """
        # full_path = os.path.join(self.current_dir, "datasets", image_path)
        full_path = image_path
        image = Image.open(full_path)
        image_transform = transforms.Compose(
            [
                transforms.Resize((256, 256)),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )

        return image_transform(image)

    def __getitem__(self, index):
        """
        Return the preprocessed image and its label at the specified index from the dataset.
        """
        image_path = self.data[index]["image:FILE"]
        label = self.data[index]["category"]

        # image_path, label = self.data[index]
        image = self.preprocess_image(image_path)
        return image, int(label)

    def __len__(self):
        """
        Return the number of items in the dataset.
        """
        return len(self.data)
