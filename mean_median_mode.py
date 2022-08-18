import numpy as np
import statistics as st

a = [3,2,2,1,3,4,3,1,1,3]

print('Mean of the array = ', np.mean(a)) # st.mean() works
# Mean = sum of array elements/number of array elements

print('Median of the array = ',np.median(a)) # st.mode() works
# Median = middle term if total no. of terms are odd.
# Median = Average of the terms in the middle (if total no. of terms are even)

print('Mode of the array = ',st.mode(a)) # BUT np.mode() DOESN'T EXIST
# Mode = Array element with maximum frequency