from fuzzy_model import FuzzyModel


class MainController:
    def __init__(self, ui):
        self.ui = ui
        self.fuzzyModel = FuzzyModel()
        self.dictTerms = {
			'Not suitable': 0,
			'Unlikely suitable': 1,
			'Maybe suitable': 2,
			'Partially suitable': 3,
			'Probably suitable': 4,
			'Excellent suitable': 5,
		}
        self.colorTerms = {
			'Not suitable': "red",
			'Unlikely suitable': "orange",
			'Maybe suitable': "gray",
			'Partially suitable': "brown",
			'Probably suitable': "green",
			'Excellent suitable': "darkgreen",
		}

    def adjust_mainWindow(self):
        self.ui.sliderResult.setEnabled(False)
        self.ui.sliderExperience.valueChanged.connect(lambda: self.move_slider(self.ui.labelExperienceValue, self.ui.sliderExperience.value()))
        self.ui.sliderDiplomScore.valueChanged.connect(lambda: self.move_slider(self.ui.labelDiplomScoreValue, self.ui.sliderDiplomScore.value()))
        self.ui.sliderProfessionalTest.valueChanged.connect(lambda: self.move_slider(self.ui.labelProfessionalTestValue, self.ui.sliderProfessionalTest.value()))
        self.ui.sliderEnglishLevel.valueChanged.connect(lambda: self.move_slider(self.ui.labelEnglishLevelValue, self.ui.sliderEnglishLevel.value()))
        self.ui.calculateButton.clicked.connect(self.calculate_suitable)

    def move_slider(self, text_label, value):
        text_label.setText(str(value))
        
    def calculate_suitable(self):
        experience = int(self.ui.sliderExperience.value())
        diplomScore = int(self.ui.sliderDiplomScore.value())
        professionalTest = int(self.ui.sliderProfessionalTest.value())
        englishLevel = int(self.ui.sliderEnglishLevel.value())
        
        termResult, numberResult = self.fuzzyModel.process(experience, diplomScore, professionalTest, englishLevel)
        
        self.ui.labelNumberResult.setText(str(numberResult) + "/10")
        self.ui.labelTermResult.setText(str(termResult))
        self.ui.sliderResult.setValue(self.dictTerms[termResult])
        self.ui.labelTermResult.setStyleSheet("QLabel { color: " + self.colorTerms[termResult] + "; }")