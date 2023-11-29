import model
import inference_mamdani

class FuzzyModel:
	def __init__(self) -> None:
		self.experience_max = 15
		self.experience_min = 0

		self.diplom_score_max = 100
		self.diplom_score_min = 60

		self.test_max = 10
		self.test_min = 0

		self.english_level_max = 10
		self.english_level_min = 0

		self.suitable_max = 10
		self.suitable_min = 0

		self.max_values = [self.experience_max, self.diplom_score_max, self.test_max, self.english_level_max]
		self.min_values = [self.experience_min, self.diplom_score_min, self.test_min, self.english_level_min]

		inference_mamdani.preprocessing(model.input_lvs, model.output_lv)
	
	def __normalization(self, x, min, max):
		return round((x - min) / (max - min), 2)

	def __denormalization(self, y, min, max):
		coef = (max - min) / (0.894390243902439 - 0.07516129032258065)
		return round((y - 0.07516129032258065) * coef + min)
	
	def process(self, experience, diplom_score, test, english_level):
		crisp = [experience, diplom_score, test, english_level]

		normalization_crisp = []
		for i in range(len(crisp)):
			normalization_value = self.__normalization(crisp[i], self.min_values[i], self.max_values[i])
			normalization_crisp.append(normalization_value)
			
		result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, normalization_crisp)
		denormalization_result = self.__denormalization(result[0], self.suitable_min, self.suitable_max)
		return (result[1], denormalization_result)


if __name__=="__main__":
	conrtoller = FuzzyModel()
	termResult, numberResult = conrtoller.process(15, 100, 10, 10)
	print(termResult, numberResult)