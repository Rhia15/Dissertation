##create heatmap 

library(aplot)
library(cowplot)
library(ggtree)
library(ggplot2)
library(dplyr)

data4 <- read.csv("/Users/rhianah/Documents/Dissertation/amphiexpand_heatmap.csv")
nodes <- read.tree("/Users/rhianah/Documents/Dissertation/r_tree2_nodes.txt")
tree <- ggtree(nodes) + geom_nodelab(size = 3, hjust = -0.2)

##change values to contracted, expanded and none 
df <- mutate(data4, Value = case_when(
  Value == "decreased" ~ "Contracted",
  Value == "increased" ~ "Expanded",
  TRUE ~ "None"
))

##keep labels in the same order 
df$label <- factor(df$label, levels = unique(df$label))
heatmap <- ggplot(df, aes(x = Genefamily, y = label)) + 
  geom_tile(aes(fill = Value), color = "black") +
  scale_fill_manual(values = c("blue", "red", "white")) +
  theme_minimal() +
  xlab("Gene Family") +  # Modify the x-axis label
  ylab(NULL) +
  theme(
    panel.grid.major = element_line(color = "white", linewidth = 1),
    panel.grid.minor = element_blank(),
    axis.text.x = element_text(angle = 90, hjust = 1, face = "bold"),
  ) + 
  scale_y_discrete(limits = rev(levels(df$label)))

##make tree 

l <- tree + geom_cladelab(node=67, label="Amphibians", align=TRUE, angle= 90, 
                         hjust= 'centre', offset.text=.5, barsize=0.5, fontsize=4) +
  geom_cladelab(node=57, label="Mammals", align=TRUE, angle=90,
                hjust = 'centre', offset.text=.5, barsize=0.5, fontsize=4) + 
  geom_cladelab(node=49, label="Birds", alighn=TRUE, angle=90, 
                hjust = 'centre', offset.text=.5, barsize=0.5, fontsize=4) +
  geom_cladelab(node=41, label="reptiles", align=TRUE, angle= 90,
                hjust= 'centre', offset.text=.5, barsize=0.5, fontsize=4)


heatmap_image <- l | heatmap
heatmap_image


# Save the plot as PNG file
ggsave("heatmap.png", plot = heatmap_image, width = 30, height = 40, dpi = 300)
dev.off()
