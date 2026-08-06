def get_project(choice):

    match choice:

        case 1:
            return r"""
% LLM Project Latex Here
"""

        case 2:
            return r"""
% CNN Latex Here
"""

        case 3:
            return r"""
% Sentiment Analysis Latex
"""

        case 4:
            return r"""
% Recommendation System Latex
"""

        case _:
            return ""