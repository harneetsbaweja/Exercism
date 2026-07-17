"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    # Arrange
    # student_scores = [1.1,2.2,5.7]
    rounded_scores = list()
    # Act
    for score in student_scores:
        int_score = round(score)
        rounded_scores.append(int_score)
    # Assert
    # print(rounded_scores)
    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    # Arrange
    # student_scores = [60,70,40]
    FAIL_SCORE = 40
    fail_count = 0
    # Act
    for score in student_scores:
        if score <= FAIL_SCORE:
            fail_count = fail_count + 1
    # Assert
    return fail_count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """
    # Arrange
    # threshold = 100
    # student_scores = [100,89]
    best_scores = list()
    # Act
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    # Assert
    # print(best_scores)
    return best_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    # Arrange
    # highest = 97
    FAIL_SCORE = 40
    NUM_GRADES = 4
    grade_list = list()
    # Act
    score_range = highest - FAIL_SCORE
    interval = score_range // NUM_GRADES

    for i in range(NUM_GRADES):
        score = FAIL_SCORE + i*interval + 1
        grade_list.append(score)

    # Assert
    # print(interval)
    # print(grade_list)
    return grade_list


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    # Arrange
    # student_scores = [96,79,54]
    # student_names = ['papa','mama','dada']
    ranked_students = list()
    # Act
    for i, student in enumerate(student_names):
        rank = str(i + 1)
        score = student_scores[i]
        # print(rank)
        # print(student)
        # print(score)
        ranked_students.append(f"{rank}. {student}: {score}")
    # Assert
    # print(ranked_students)
    return ranked_students

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    # Arrange
    # student_info = [['a',99],['b',75],['c',10]]
    SCORE_INDEX = 1
    perfect_student = []
    # Act
    for i,_ in enumerate(student_info):
        perfect_student = student_info[i]
        if perfect_student[SCORE_INDEX] == 100:
            break
        else:
            perfect_student = []
    # Assert
    # print(perfect_student)
    return perfect_student