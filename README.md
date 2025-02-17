# Homework 3 - Packages, Data files, Matplotlib

This homework consists of 8 questions in **Homework3_ProblemSet.ipynb** and a 9th request to update this repository.

**Step 1** Complete the notebook questions.

**Step 2** Update this README to include the figures generated in questions Q6 - Q8 and with the information reqested in Q9. Your README should include four short paragraphs that describe these plots and what you learned from them:
*The first paragraph should describe the data set. 
*The second paragraph should describe the Figure from Q6.
*The third paragraph should describe the Figure from Q7, and 
*The fourth paragraph should describe the Figure Q8.  

Make sure to include the names of the figures in your descriptions, and make sure that your descriptions are clear and easy to understand.  You should also include a short paragraph at the end of the README that describes how you completed this assignment, including listing any resources that you used.



The dataset used in this analysis is the Breast Cancer Wisconsin (Diagnostic) Dataset, which contains 30 numerical features derived from digitized images of breast mass cell nuclei. Each sample is classified as either Malignant (M) or Benign (B). Malignant tumors are cancerous and more likely to spread, while benign tumors are non-cancerous and typically less dangerous. The features describe various properties of the cell nuclei, such as radius, texture, perimeter, area, and smoothness. This dataset helps in understanding the differences between malignant and benign tumors based on these measurable characteristics.

C:\Users\krose\OneDrive\Documents\GitHub\480A5CourseMaterials\homework3-Ktitus9\q6.png
Figure 1: Histogram of a Key Feature
This histogram compares the distribution of a selected feature for malignant and benign tumors. Malignant tumors tend to have higher values for this feature, highlighting a key difference between the two classes.

Figure 1 presents a histogram comparing the distributions of a selected feature (e.g., mean perimeter) for Malignant and Benign tumors. The histogram uses different colors for each tumor type to highlight differences in their distributions. From the plot, we observe that malignant tumors tend to have larger perimeters than benign tumors. This indicates that certain features, such as tumor size-related properties, may serve as strong indicators for distinguishing between cancerous and non-cancerous masses.

C:\Users\krose\OneDrive\Documents\GitHub\480A5CourseMaterials\homework3-Ktitus9\q7.jpg
Figure 2: Scatter Plot of Two Features
This scatter plot visualizes the relationship between two features, with benign tumors shown as red circles and malignant tumors as blue squares. The plot reveals distinct clustering, indicating that these features help differentiate between the two tumor types.

Figure 2 shows a scatter plot comparing two selected features (e.g., mean area vs. mean perimeter), with benign tumors represented as red circles and malignant tumors represented as blue squares. The goal was to choose features where the separation between the two tumor types is as distinct as possible. The scatter plot reveals that malignant tumors generally occupy a different region in the feature space compared to benign tumors, suggesting that these features could be useful for classification. However, some overlap remains, indicating that a combination of multiple features or advanced techniques like PCA may further improve separation.

C:\Users\krose\OneDrive\Documents\GitHub\480A5CourseMaterials\homework3-Ktitus9\q8.jpg
Figure 3: PCA Scatter Plot
This scatter plot displays the first two principal components of the dataset after applying PCA. The separation of benign and malignant tumors suggests that most of the dataset’s variance can be captured in just two dimensions, making classification possible with reduced complexity.

Figure 3 displays a scatter plot of the first two principal components after applying Principal Component Analysis (PCA) to the dataset. Each tumor type is again represented using the same color and marker scheme as in Figure 2. PCA reduces the dataset’s dimensionality while retaining most of the variance, making it useful for visualization. The plot shows that malignant and benign tumors form distinguishable clusters, confirming that the dataset’s features contain meaningful patterns for classification. However, the presence of some overlapping points indicates that no single transformation can perfectly separate the two groups, emphasizing the importance of using multiple classification methods.

I completed this assignment with help from the in-class notes and debugging/problem-solving from Copilot AI and ChatGPT. I completed the problems over the course of a few days. I did not recieve help from any classmates, nor did I give any assistance to classmates. I also did not recieve help from any instructors/TAs.
