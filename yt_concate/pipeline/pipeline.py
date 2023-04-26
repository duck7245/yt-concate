from .steps.step import StepException  # 相對路徑


class Pipeline:  # 沒有繼承 step

    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None  # 投入的參數, 也可放在 main 裡, 就像 inputs 是放在 main 裡, 新加 data 參數的主因是為了傳遞 data 給下一個process (只是接受 data 就不用)
        for step in self.steps:
            try:
                data = step.process(data, inputs)
                print(len(data))
                # data = step.process(inputs)
                # print(len(data))

            except StepException as e:
                print('Exception happened:', e)
                break
