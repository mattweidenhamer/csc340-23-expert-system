import json

class Expert:
    def __init__(self, kb_path, dialogue_path):
        self.kb_path = kb_path
        self.dialogue_path = dialogue_path
        self.contributed = False
        with open(self.kb_path) as kb_file:
            self.kb = json.load(kb_file)
        with open(self.dialogue_path) as d_file:
            self.dialogue = json.load(d_file)

    def start(self):
        print(self.dialogue["intro"])
        while(True):
            a1 = self.string_question(self.dialogue["q1"])
            a2 = self.string_question(self.dialogue["q2"])
            a3 = self.yes_or_no_question(self.dialogue["q3"])
            result_str = a1 + "-" + a2 + "-"
            if a3:
                result_str += "1"
            else:
                result_str += "0"
            self.manage_answer(result_str)
            if not self.yes_or_no_question(self.dialogue["repeat"]):
                break
        print(self.dialogue['farewell'])
        if(self.contributed):
            self.export_kb()
            print(self.dialogue['contribution'])

    def yes_or_no_question(self, prompt):
        while(True):
            result = input(prompt)
            if result.lower() in ("yes", "y"):
                return True
            if result.lower() in ("no", "n"):
                return False
            print(self.dialogue["cant_understand"])

    def string_question(self, prompt, force_lower = True):
        if force_lower:
            return input(prompt).lower()
        return input(prompt)

    def manage_answer(self, user_string):
        print(user_string)
        if user_string in self.kb:
            answers = self.kb[user_string]["names"]
            done_one = False
            for answer in answers:
                if not done_one:
                    done_one = True
                    print(f"{self.dialogue['conclusion']}{answer}")
                else:
                    print(f"{self.dialogue['multiple_conclusion']}{answer}")
            if not self.yes_or_no_question(self.dialogue['confirmation']):
                self.add_new_element(user_string)
        else:
            print(self.dialogue["not_found"])
            self.add_new_element(user_string)

    def add_new_element(self, user_string):
        self.contributed = True
        new_entry = self.string_question(self.dialogue["request_entry"], force_lower=False)
        if user_string in self.kb:
            self.kb[user_string]["names"].append(new_entry)
        else:
            self.kb[user_string] = {"names" : [new_entry]}


    def export_kb(self):
        with open(self.kb_path, "w") as kb_file:
            json.dump(self.kb, kb_file, indent=4)


def main():
    pass

if __name__ == "__main__":
    main()