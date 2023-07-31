G122 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_122.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G122$Domain, G122$Lineage)
print(frequency_table)


df_frequency <- as.data.frame(as.table(frequency_table))
df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

df_formatted

library(reshape2)
df_melted <- melt(df_formatted, id.vars = "Var1")


archi122 <- ggplot(df_melted, aes(x = value, y = Var1, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 122",
       x = "Counts",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  scale_fill_manual(values = c("orange", "blue")) + 
  theme(axis.text.y = element_text(hjust = 1, size = 11),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))  # Adjust y-axis labels alignment

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/122_archi.png", plot = archi122, width = 10, height = 8, dpi = 300)



G58 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_58.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G58$Domain, G58$Lineage)
print(frequency_table)


df_frequency <- as.data.frame(as.table(frequency_table))


df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

df_formatted

library(reshape2)
df_melted <- melt(df_formatted, id.vars = "Var1")


arhi58 <- ggplot(df_melted, aes(x = value, y = Var1, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 58",
       x = "Counts",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  scale_fill_manual(values = c("orange", "blue")) + 
  theme(axis.text.y = element_text(hjust = 1, size = 11),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))  # Adjust y-axis labels alignment

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/58_archi.png", plot = arhi58, width = 10, height = 8, dpi = 300)


##73

#make into frequency table

G73 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_73.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G73$Domain, G73$Lineage)
print(frequency_table)

df_frequency <- as.data.frame(as.table(frequency_table))

df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

df_formatted

library(reshape2)
df_melted <- melt(df_formatted, id.vars = "Var1")


 archi73 <- ggplot(df_melted, aes(x = value, y = Var1, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 73",
       x = "Counts",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  scale_fill_manual(values = c("orange", "blue")) + 
  theme(axis.text.y = element_text(hjust = 1, size = 11),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))  # Adjust y-axis labels alignment

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/73_archi.png", plot = archi73, width = 10, height = 8, dpi = 300)


#######68


G68 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_68.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G68$Domain, G68$Lineage)
print(frequency_table)

df_frequency <- as.data.frame(as.table(frequency_table))


df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

df_formatted

library(reshape2)
df_melted <- melt(df_formatted, id.vars = "Var1")


archi68 <- ggplot(df_melted, aes(x = value, y = Var1, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 68",
       x = "Counts",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  scale_fill_manual(values = c("orange", "blue")) + 
  theme(axis.text.y = element_text(hjust = 1, size = 11),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))  # Adjust y-axis labels alignment

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/68_archi.png", plot = archi68, width = 10, height = 8, dpi = 300)


#######17


G17 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_17.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G17$Domain, G17$Lineage)
print(frequency_table)

df_frequency <- as.data.frame(as.table(frequency_table))


df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

df_formatted

library(reshape2)
df_melted <- melt(df_formatted, id.vars = "Var1")


archi17 <- ggplot(df_melted, aes(x = value, y = Var1, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 17",
       x = "Counts",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  scale_fill_manual(values = c("orange", "blue")) + 
  theme(axis.text.y = element_text(hjust = 1, size = 11),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))  # Adjust y-axis labels alignment

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/17_archi.png", plot = archi17, width = 10, height = 8, dpi = 300)

####orthogroup 7 and 54 

G7 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_07.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G7$Domain, G7$Lineage)
print(frequency_table)

df_frequency <- as.data.frame(as.table(frequency_table))

df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

df_formatted

library(reshape2)
df_melted <- melt(df_formatted, id.vars = "Var1")


ggplot(df_melted, aes(x = value, y = Var1, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 7",
       x = "Counts",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  scale_fill_manual(values = c("orange", "blue")) + 
  theme(axis.text.y = element_text(hjust = 1, size = 11),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))  # Adjust y-axis labels alignment

ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/7_archi.png", plot = G73plot, width = 10, height = 8, dpi = 300)

####orthogroup 1225

G1255 <- read.table("/Users/rhianah/Documents/Dissertation/domain_mapping/combined_1255.tsv", header = TRUE, sep = "\t")
frequency_table <- table(G1255$Domain, G1255$Lineage)
print(frequency_table)

df_frequency <- as.data.frame(as.table(frequency_table))


df_formatted <- df_frequency %>%
  pivot_wider(names_from = Var2, values_from = Freq, values_fill = 0) %>%
  arrange(Var1)

df_formatted

library(reshape2)
df_melted <- melt(df_formatted, id.vars = "Var1")

# Create the horizontal bar chart
g1255 <- ggplot(df_melted, aes(x = value, y = Var1, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Orthogroup 1255",
       x = "Counts",
       y = "Protein Domain (PFAM)",
       fill = "Group") +
  scale_fill_manual(values = c("orange", "blue")) + 
  theme(axis.text.y = element_text(hjust = 1, size = 11),  # Set the y-axis label size to 12
        axis.text.x = element_text(size = 12),             # Set the x-axis label size to 12
        plot.title = element_text(hjust = 0.5, size = 20),  # Center the title and set the title size to 16
        axis.title = element_text(size = 15))  # Adjust y-axis labels alignment

g1255


ggsave(filename = "/Users/rhianah/Documents/Dissertation/domain_mapping/1255_archi.png", plot = g1255, width = 10, height = 8, dpi = 300)

