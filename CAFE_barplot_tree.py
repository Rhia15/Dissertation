##make gene birth and death tree showing cafe results 

tree <- read.tree("/Users/rhianah/Documents/Dissertation/finaltree_correctednames_R.txt")
tree <- ggtree(tree) + theme_tree2() + scale_x_continuous(labels = abs)
tree

#add time scale 
p1 <- revts(tree)
p1


##add increase and decrease values 
annoted_data <- read.csv("/Users/rhianah/Documents/Dissertation/node_test3.csv")
annoted_data2 <- read.csv("/Users/rhianah/Documents/Dissertation/node_test3.1.csv")
p <- tree %<+% annoted_data2 + 
  geom_text(aes(x=branch, label = paste(decrease, increase, sep = "/")), vjust=2, size = 3) +
  geom_tiplab(size = 3, hjust = 0) + labs(title= "Gene birth and death") +
  theme(plot.title = element_text(face = "bold", hjust = 0.5))

p

##add on bar plots

data <- read.csv("/Users/rhianah/Documents/Dissertation/nodes_tree.csv")

bars <- nodebar(data, cols=2:3, position='dodge',
                color=c(increase='red', decrease='blue'))


barplot <- inset(tree, bars, x='branch', width=0.02, vjust=-0.25, height = 0.02)
barplot

barplot2 <- inset(p1, bars, x='branch', width=0.02, vjust=-0.25, height = 0.02)
barplot2

ggsave(filename = "/Users/rhianah/Documents/Dissertation/tree_with_barplot.png", 
       plot = barplot, 
       width = 10, height = 8, units = "cm", dpi = 300,
       scale = 1.2)
