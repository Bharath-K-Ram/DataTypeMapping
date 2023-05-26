# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 12:54 PM 24/05/23 using PyCharm

# Numeric constants
SAMPLE_SIZE = 2000
SIMILARITY_THRESHOLD = 0.60

# Regex pattern constants
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
URL_REGEX = r'(?:https?|ftp)://[\w\-]+(?:\.[\w\-]+)+(?::\d+)?(?:/[^\s]*)?'
IMAGE_REGEX = r'([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)'

# Logging levels
INFO = "INFO"
DEBUG = "DEBUG"
EXCEPTION = "EXCEPTION"
ERROR = "ERROR"

# Crm data types
OTHER = "Other"
SINGLE_LINE = "single_line"
EMAIL = "email"
PHONE = "phone"
CURRENCY = "currency"
DATE = "date"
DATE_TIME = "date_time"
URL = "url"
DECIMAL = "decimal"
CHECKBOX = "check_box"
MULTI_SELECT = "multi_select"
PICK_LIST = "pick_list"
USER = "user"
FILE_UPLOAD = "file_upload"
NUMBER = "number"
AUTO_NUMBER = "auto_number"
IMAGE = "image"
PERCENTAGE = "percentage"
LONG_INTEGER = "long_integer"
FORMULAE = "formulae"
MULTI_LINE = "multi_line"

# Default Crm Specific for Single line data type
NAME = "name"
F_NAME = "first_name"
L_NAME = "last_name"
COMPANY = "company"
ADDRESS = "address"
STATE = "state"
CITY = "city"
COUNTRY = "country"
STREET = "street"
ZIPCODE = "zip code"
TITLE = "title"

# List of data types and single line data type for column wise similarity checking
DATA_TYPE_LIST = [EMAIL, PHONE, IMAGE, FORMULAE, URL, DATE, DATE_TIME, CURRENCY]
SINGLE_LINE_VALUES = [NAME, F_NAME, L_NAME, COUNTRY, COMPANY, CITY, STATE, STREET, ADDRESS, TITLE, ZIPCODE]

# Sampling techniques
SYS_RANDOM_SAMPLING = "systematic_random_sampling"
RANDOM_SAMPLING = "random_sampling"
STRATIFIED_SAMPLING = "stratified_sampling"
CLUSTER_SAMPLING = "cluster_sampling"
