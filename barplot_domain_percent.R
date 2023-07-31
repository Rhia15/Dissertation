
#make into frequency table

G122 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_122.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G122$Domain, G122$Lineage)
print(frequency_table)


#  Convert the frequency table to a data frame
df_frequency <- as.data.frame(as.table(frequency_table))

# Reshape the data frame to the desired format
df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

# Save the formatted data frame to a CSV file
write.csv(df_formatted, file = "/Users/rhianah/Documents/Dissertation/domain_mapping/G122_archi.csv", row.names = FALSE)

library(ggplot2)

# Read CSV file into a dataframe
file_path <- "/Users/rhianah/Documents/Dissertation/domain_mapping/G122_percentage.csv"
df <- read.csv(file_path, row.names = NULL)

# Reshape the data to a longer format
library(reshape2)
df_melted <- melt(df, id.vars = "PFAM")

# Create horizontal bar chart
G122plot <- ggplot(df_melted, aes(x = value, y = PFAM, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 122",
       x = "Percentage",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  theme(axis.text.y = element_text(hjust = 1, size = 12),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))


#save plot

# Save the plot as a PNG file
ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/122.png", plot = G122plot, width = 10, height = 8, dpi = 300)


###58 



#make into frequency table

G58 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_58.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G58$Domain, G58$Lineage)
print(frequency_table)


# Step 3: Convert the frequency table to a data frame
df_frequency <- as.data.frame(as.table(frequency_table))

# Step 4: Reshape the data frame to the desired format
df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

# Step 5: Save the formatted data frame to a CSV file
write.csv(df_formatted, file = "/Users/rhianah/Documents/Dissertation/domain_mapping/G58_archi.csv", row.names = FALSE)

library(ggplot2)

# Read the CSV file into a dataframe
file_path <- "/Users/rhianah/Documents/Dissertation/domain_mapping/G58_percentage.csv"
df <- read.csv(file_path, row.names = NULL)

# Reshape the data to a longer format
library(reshape2)
df_melted <- melt(df, id.vars = "PFAM")

# Create the horizontal bar chart
G58plot <- ggplot(df_melted, aes(x = value, y = PFAM, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 58",
       x = "Percentage",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  theme(axis.text.y = element_text(hjust = 1, size = 12),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))

G58plot

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/58.png", plot = G58plot, width = 10, height = 8, dpi = 300)

###73

#make into frequency table

G73 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_73.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G73$Domain, G73$Lineage)
print(frequency_table)


# Step 3: Convert the frequency table to a data frame
df_frequency <- as.data.frame(as.table(frequency_table))

# Step 4: Reshape the data frame to the desired format
df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

# Step 5: Save the formatted data frame to a CSV file
write.csv(df_formatted, file = "/Users/rhianah/Documents/Dissertation/domain_mapping/G73_archi.csv", row.names = FALSE)

library(ggplot2)

# Read the CSV file into a dataframe
file_path <- "/Users/rhianah/Documents/Dissertation/domain_mapping/G73_percentage.csv"
df <- read.csv(file_path, row.names = NULL)

# Reshape the data to a longer format
library(reshape2)
df_melted <- melt(df, id.vars = "PFAM")

# Create the horizontal bar chart
G73plot <- ggplot(df_melted, aes(x = value, y = PFAM, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 73",
       x = "Percentage",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  theme(axis.text.y = element_text(hjust = 1, size = 11),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))

G73plot

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/73.png", plot = G73plot, width = 10, height = 8, dpi = 300)



#######68


G68 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_68.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G68$Domain, G68$Lineage)
print(frequency_table)


# Step 3: Convert the frequency table to a data frame
df_frequency <- as.data.frame(as.table(frequency_table))

# Step 4: Reshape the data frame to the desired format
df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

# Step 5: Save the formatted data frame to a CSV file
write.csv(df_formatted, file = "/Users/rhianah/Documents/Dissertation/domain_mapping/G68_archi.csv", row.names = FALSE)

library(ggplot2)

# Read the CSV file into a dataframe
file_path <- "/Users/rhianah/Documents/Dissertation/domain_mapping/G68_percentage.csv"
df <- read.csv(file_path, row.names = NULL)

# Reshape the data to a longer format
library(reshape2)
df_melted <- melt(df, id.vars = "PFAM")

# Create the horizontal bar chart
G68plot <- ggplot(df_melted, aes(x = value, y = PFAM, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 68",
       x = "Percentage",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  theme(axis.text.y = element_text(hjust = 1, size = 12),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))

G68plot

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/68.png", plot = G68plot, width = 10, height = 8, dpi = 300)


#######17


G17 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_17.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G17$Domain, G17$Lineage)
print(frequency_table)


# Step 3: Convert the frequency table to a data frame
df_frequency <- as.data.frame(as.table(frequency_table))

# Step 4: Reshape the data frame to the desired format
df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

# Step 5: Save the formatted data frame to a CSV file
write.csv(df_formatted, file = "/Users/rhianah/Documents/Dissertation/domain_mapping/G17_archi.csv", row.names = FALSE)

library(ggplot2)

# Read the CSV file into a dataframe
file_path <- "/Users/rhianah/Documents/Dissertation/domain_mapping/G17_percentage.csv"
df <- read.csv(file_path, row.names = NULL)

# Reshape the data to a longer format
library(reshape2)
df_melted <- melt(df, id.vars = "PFAM")

# Create the horizontal bar chart
G17plot <- ggplot(df_melted, aes(x = value, y = PFAM, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 17",
       x = "Percentage",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  theme(axis.text.y = element_text(hjust = 1, size = 12),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))

G17plot

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/17.png", plot = G17plot, width = 10, height = 8, dpi = 300)



####orthogroup 7 and 54 

G7 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_07.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G7$Domain, G7$Lineage)
print(frequency_table)


# Step 3: Convert the frequency table to a data frame
df_frequency <- as.data.frame(as.table(frequency_table))

# Step 4: Reshape the data frame to the desired format
df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

# Step 5: Save the formatted data frame to a CSV file
write.csv(df_formatted, file = "/Users/rhianah/Documents/Dissertation/domain_mapping/7_archi.csv", row.names = FALSE)


G54 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_54.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G54$Domain, G54$Lineage)
print(frequency_table)


# Step 3: Convert the frequency table to a data frame
df_frequency <- as.data.frame(as.table(frequency_table))

# Step 4: Reshape the data frame to the desired format
df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

# Step 5: Save the formatted data frame to a CSV file
write.csv(df_formatted, file = "/Users/rhianah/Documents/Dissertation/domain_mapping/G54_archi.csv", row.names = FALSE)


###attempting stacked barplot

# Load the required packages
library(tidyverse)

# Sample data (replace this with your actual data)
data <- data.frame(
  Orthogroup = c("Orthogroup7", "Orthogroup7", "Orthogroup54", "Orthogroup54"),
  PFAM = c("7tm_4", "Trypsin", "7tm_4", "Unknown"),
  Amphibian = c(177, 0, 388, 0),
  Amniote = c(796, 0, 2, 5),
  Amphiban = c(388, 1, 0, 3),
  Amniote_2 = c(2, 0, 0, 0)
)

# Transpose the data and convert it to long format
data_long <- data %>%
  pivot_longer(cols = starts_with("Am"), names_to = "Amniote_Group", values_to = "Value")

# Create the stacked barplot
ggplot(data_long, aes(x = Orthogroup, y = Value, fill = PFAM)) +
  geom_bar(stat = "identity", position = "stack") +
  facet_grid(Amniote_Group ~ ., scales = "free_y", switch = "y") +
  labs(title = "Stacked Barplot", x = "Orthogroups", y = "Count") +
  theme_minimal()




#####1255

G1255 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_1255.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G1255$Domain, G1255$Lineage)
print(frequency_table)


# Step 3: Convert the frequency table to a data frame
df_frequency <- as.data.frame(as.table(frequency_table))

# Step 4: Reshape the data frame to the desired format
df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

# Step 5: Save the formatted data frame to a CSV file
write.csv(df_formatted, file = "/Users/rhianah/Documents/Dissertation/domain_mapping/G1255_.csv", row.names = FALSE)

# Read the CSV file into a dataframe
file_path <- "/Users/rhianah/Documents/Dissertation/domain_mapping/G1255_percentage.csv"
df <- read.csv(file_path, row.names = NULL)

# Reshape the data to a longer format
library(reshape2)
df_melted <- melt(df, id.vars = "PFAM")

# Create the horizontal bar chart
G1255plot <- ggplot(df_melted, aes(x = value, y = PFAM, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 1255",
       x = "Percentage",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  theme(axis.text.y = element_text(hjust = 1, size = 12),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))

G1255plot

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/1255.png", plot = G1255plot, width = 10, height = 8, dpi = 300)
