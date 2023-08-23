import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer

# to access the file
def access_file(file_path, file_format):
	if file_format == 'csv':
		data = pd.read_csv(file_path)
	elif file_format == 'excel':
		data = pd.read_excel(file_path)
	elif file_format == 'sql':
		# I can't handle this part now
		pass
	else:
		raise ValueError("Invalid file format")
	return data


def data_preprocessing(data):
	# Handle missing values in numerical columns
	numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
	imputer_num = SimpleImputer(strategy='mean')
	data[numerical_cols] = imputer_num.fit_transform(data[numerical_cols])

	# Handle missing values in categorical columns
	categorical_cols = data.select_dtypes(include=['object']).columns
	imputer_obj = SimpleImputer(strategy='constant', fill_value='Unknown')
	data[categorical_cols] = imputer_obj.fit_transform(data[categorical_cols])

	return data

def printing_data(data):
	print('*'*50)
	print(f"columns of file are :\n {data.columns}")
	print('*'*50)
	print(f"file shape is :  {data.shape}")
	print('*'*50)
	print(f"file null values before handling  : \n {data.isnull().sum()}")
	print('*'*50)
	data_preprocessing(data)
	print(f"file null values after handling  : \n {data.isnull().sum()}")
	print('*'*50)


def generate_visualizations(data):
	for col in data.columns:
		plt.figure()
		if data[col].dtype in ['int64', 'float64']:
			sns.histplot(data[col])
			plt.title(f'Histogram of {col}')
			plt.show()
			plt.pie(data[col].value_counts())
			plt.title(f"pie chart of {col}")
			plt.show()

		elif data[col].dtype == 'datetime64[ns]':
			sns.lineplot(data=data, x=col, y='Total')
			plt.title(f'{col} vs Total')
			plt.show()

file_format=input("please enter file type (csv,excel) ")
file_path=input("please enter file path")
data = access_file(file_path, file_format)
print(data)

printing_data(data)
data = data_preprocessing(data)
generate_visualizations(data)