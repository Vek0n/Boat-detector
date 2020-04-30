from pathlib import Path


class Config:
    def __init__(self, input_img, model, precisionX, precisionY , save_fig):
        self.input_path = Path("TestPython/input/") / input_img
        self.model_path = Path("TestPython/models/") / model
        self.precisionX = precisionX
        self.precisionY = precisionY
        self.save_fig = "TestPython/output/" + save_fig

    def get_input(self):
        return self.input_path

    def get_model(self):
        return self.model_path

    def get_precisionX(self):
        return self.precisionX

    def get_precisionY(self):
        return self.precisionY

    def get_savefig(self):
        return self.save_fig
