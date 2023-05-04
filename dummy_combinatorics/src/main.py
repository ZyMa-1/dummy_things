from dummy_combinatorics.src.ColorFormatter import Colored
from dummy_combinatorics.src.combinatorics import cumulative_probability

if __name__ == "__main__":
    total_cases = 400
    prob_knife = 0.0025
    res_knife = 1
    p1 = Colored(res_knife, 'blue')
    p2 = Colored(total_cases, 'red')
    p3 = Colored(prob_knife * 100, 'yellow', is_percentage=True)
    p4 = Colored(cumulative_probability(prob=prob_knife, res=res_knife, total=total_cases) * 100, 'yellow',
                 is_percentage=True)
    print("Probabily of opening at least {} knifes in csgo in {} cases "
          "with {} probability is approximately ~{:.100f}".format(p1, p2, p3, p4))
