#1
import pandas as pd

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_csv(self):
        self.data = pd.read_csv(self.file_path)

    def display_data(self):
        if self.data is not None:
            for index, row in self.data.iterrows():
                student_name = row['Tên sinh viên']
                hp1 = row['HP 1']
                hp2 = row['HP 2']
                hp3 = row['HP 3']
                print(f"Student: {student_name}, HP1: {hp1}, HP2: {hp2}, HP3: {hp3}")


#  Chuyển đổi list thành một mảng NumPy để thực hiện các phân tích.Phân Tích Điểm Số


    def convert_to_grades(self):
        def get_grade(score):
            if 8.5 <= score <= 10:
                return 'A'
            elif 8.0 <= score < 8.5:
                return 'B+'
            elif 7.0 <= score < 8.0:
                return 'B'
            elif 6.5 <= score < 7.0:
                return 'C+'
            elif 5.5 <= score < 6.5:
                return 'C'
            elif 5.0 <= score < 5.5:
                return 'D+'
            elif 4.0 <= score < 5.0:
                return 'D'
            else:
                return 'F'

        if self.data is not None:
            for col in ['HP 1', 'HP 2', 'HP 3']:
                self.data[f'{col} Grade'] = self.data[col].apply(get_grade)

    def display_grades(self):
        if self.data is not None:
            for index, row in self.data.iterrows():
                student_name = row['Tên sinh viên']
                hp1_grade = row['HP 1 Grade']
                hp2_grade = row['HP 2 Grade']
                hp3_grade = row['HP 3 Grade']
                print(f"Student: {student_name}, HP1 Grade: {hp1_grade}, HP2 Grade: {hp2_grade}, HP3 Grade: {hp3_grade}")

    def convert_to_numpy(self):
        if self.data is not None:
            return self.data[['HP 1', 'HP 2', 'HP 3']].to_numpy()
#3 chia tách học phần  
    def split_by_subject(self):
        if self.data is not None:
            subjects = {}
            for col in ['HP 1', 'HP 2', 'HP 3']:
                subjects[col] = self.data[['Tên sinh viên', col, f'{col} Grade']]
            return subjects    
# 4 phân tích tổng, trung bình , độ lệch chuẩn của mỗi học phần
    # Phân tích tổng, trung bình và độ lệch chuẩn cho mỗi học phần
    def analyze_scores(self):
        if self.data is not None:
            analysis = {}
            for col in ['HP 1', 'HP 2', 'HP 3']:
                total = self.data[col].sum()  # Tổng điểm
                mean = self.data[col].mean()  # Trung bình
                std_dev = self.data[col].std()  # Độ lệch chuẩn
                analysis[col] = {
                    'Tổng': total,
                    'Trung bình': mean,
                    'Độ lệch chuẩn': std_dev
                }
            return analysis    
#5 Tính toán số lượng sinh viên đạt từng loại điểm chữ (A, B+, B,...) trên tổng số học phần
    def count_grades(self):
        if self.data is not None:
            grade_counts = {'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D+': 0, 'D': 0, 'F': 0}
            
            # Đếm số lượng sinh viên đạt từng loại điểm chữ cho từng học phần
            for col in ['HP 1', 'HP 2', 'HP 3']:
                for grade in grade_counts.keys():
                    grade_counts[grade] += (self.data[f'{col} Grade'] == grade).sum()
            
            # Tính tỷ lệ đạt từng loại điểm chữ trên tổng số học phần
            total_subjects = len(['HP 1', 'HP 2', 'HP 3'])
            total_students = len(self.data)
            grade_percentages = {grade: (count / (total_subjects * total_students)) * 100 for grade, count in grade_counts.items()}
            
            return grade_counts, grade_percentages    
# Sử dụng lớp CSVReader
path = 'D:/17A1KHDL/lab2/Data/diem_hoc_phan.csv'
reader = CSVReader(path)
reader.read_csv()
reader.display_data()

# Quy đổi điểm số sang điểm chữ
reader.convert_to_grades()
print("\nDanh sách điểm chữ:")
reader.display_grades()
# Chuyển đổi dữ liệu thành mảng NumPy
numpy_array = reader.convert_to_numpy()
print("\nMảng NumPy của điểm số:")
print(numpy_array)
# Chia tách dữ liệu theo học phần
split_data = reader.split_by_subject()
print("\nDữ liệu theo từng học phần:")
for subject, data in split_data.items():
    print(f"\n{subject}:")
    print(data)
# Phân tích tổng, trung bình và độ lệch chuẩn cho mỗi học phần
analysis = reader.analyze_scores()
print("\nPhân tích tổng, trung bình và độ lệch chuẩn cho mỗi học phần:")
for subject, stats in analysis.items():
    print(f"\n{subject}:")
    print(f"Tổng: {stats['Tổng']}, Trung bình: {stats['Trung bình']}, Độ lệch chuẩn: {stats['Độ lệch chuẩn']}")    
# Tính toán số lượng sinh viên đạt từng loại điểm chữ
grade_counts, grade_percentages = reader.count_grades()
print("\nSố lượng sinh viên đạt từng loại điểm chữ trên tổng số học phần:")
for grade, count in grade_counts.items():
    print(f"{grade}: {count} sinh viên")

print("\nTỷ lệ phần trăm sinh viên đạt từng loại điểm chữ:")
for grade, percentage in grade_percentages.items():
    print(f"{grade}: {percentage:.2f}%")
        