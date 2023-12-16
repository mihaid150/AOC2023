class OasisReport:
    def __init__(self, input_data):
        self.input_data = input_data.splitlines()
        self.oasis_histories = []

    def process_input_data(self):
        for line in self.input_data:
            numbers = line.split()
            self.oasis_histories.append([int(number) for number in numbers])

    @staticmethod
    def check_local_history(history):
        check = True
        check &= all(n == 0 for n in history)
        return check

    def find_history_elements(self):
        self.process_input_data()
        history_sum = 0

        for oasis_history in self.oasis_histories:
            local_history = [oasis_history]

            while True:
                if self.check_local_history(local_history[-1]):
                    break
                current_list = local_history[-1]
                differences = [current_list[i + 1] - current_list[i] for i in range(len(current_list) - 1)]
                local_history.append(differences)

            local_history[-1].append(0)
            local_history = list(reversed(local_history))
            for i in range(0, len(local_history) - 1):
                local_history[i + 1].append(local_history[i][-1] + local_history[i+1][-1])

            history_sum += local_history[-1][-1]

        print(history_sum)

    def find_history_elements_backward(self):
        self.process_input_data()
        history_sum = 0

        for oasis_history in self.oasis_histories:
            local_history = [oasis_history]

            while True:
                if self.check_local_history(local_history[-1]):
                    break
                current_list = local_history[-1]
                differences = [current_list[i + 1] - current_list[i] for i in range(len(current_list) - 1)]
                local_history.append(differences)

            local_history[-1] = [0] + local_history[-1]
            local_history = list(reversed(local_history))
            for i in range(0, len(local_history) -1):
                local_history[i + 1] = [local_history[i + 1][0] - local_history[i][0]] + local_history[i + 1]

            history_sum += local_history[-1][0]

        print(history_sum)

