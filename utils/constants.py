# from distances.dtw.dtw import dynamic_time_warping as dtw
# import pyximport
# pyximport.install()
from distances.dtw.dtw import dynamic_time_warping as dtw
from dba import dba
from kmeans import kmeans

UNIVARIATE_DATASET_NAMES = ['CinC_ECG_torso','ECG200','ECG5000','ECGFiveDays','NonInvasiveFatalECG_Thorax1','NonInvasiveFatalECG_Thorax2','TwoLeadECG']

UNIVARIATE_ARCHIVE_NAMES = ['UCR_TS_Archive_2015']

AVERAGING_ALGORITHMS = {'dba':dba }

CLUSTERING_ALGORITHMS = {'kmeans':kmeans}

CLASSIFIERS = ['fcn'] #resnet25, resnet50, COTE, ResNext

ITERATIONS = 1

DISTANCE_ALGORITHMS = {'dtw': dtw } # I want to incoroporate soft-dtw soon
DTW_PARAMS = {'w':0} # warping window should be given in percentage (negative means no warping window)
DISTANCE_ALGORITHMS_PARAMS = {'dtw':DTW_PARAMS }

MAX_PROTOTYPES_PER_CLASS = 5 # 2x most represented class, 2x dataset size

NB_ITERATIONS = 5

dataset_types = {'NonInvasiveFatalECG_Thorax2':'ECG',
'NonInvasiveFatalECG_Thorax1':'ECG',
'ECG5000':'ECG',
'ECG200':'ECG',
'CinC_ECG_torso':'ECG',
'ECGFiveDays':'ECG',
'TwoLeadECG':'ECG'}

themes_colors ={'ECG':'green'}