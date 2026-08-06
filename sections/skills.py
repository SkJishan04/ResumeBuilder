def get_skills(choice):

    match choice:

        case 1:
            return r"""
% AIML Skills Latex
"""

        case 2:
            return r"""
% Data Analytics Skills
"""

        case 3:
            return r"""
% LLM Skills
"""

        case 4:
            return r"""
% Full Stack Skills
"""

        case _:
            return ""