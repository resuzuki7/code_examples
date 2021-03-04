pacman::p_load(tidyverse)
theme_set(theme_minimal())

files <- list.files("prod")

i <- 1

for (i in 1:length(files)){
  filename <- files[i]
  temp <- read.csv(paste("prod/", filename, sep=""), header=T, stringsAsFactors=F)

  write.csv(temp[c("Name", "SKU", "Quantity", "Product.Family.Code", "Price", "Special.Price", "status")] %>%
#              filter(Attribute.Set == 9) %>%
              mutate(discount = (Price - Special.Price)/Price,
                     "SKUcomma" = paste(SKU, ",", sep = "")) %>%
              arrange(desc(Quantity))
            ,
            paste("clean/c_", filename[1], sep=""),
            row.names =FALSE)
}


p_data <- temp %>%
  mutate(discount = (Price - Special.Price)/Price,
         "SKUcomma" = paste(SKU, ",", sep = "")) %>%
  arrange(desc(Quantity))

p_data %>%
  ggplot(aes(x = "identity", y=discount)) +
  geom_boxplot(outlier.alpha = 0) +
  geom_jitter(alpha = 0.15) + 
  geom_hline( linetype = "dashed", yintercept = 0.9, alpha = 0.3) + 
  ylim(0,1)



pattern <- "^[0-9][0-9][0-9][0-9][0-9]$"
paste(p_data[p_data$Quantity > 20, ]$SKU %>% str_subset(pattern)
      , collapse=", ", sep="")

paste(p_data$SKU , collapse=", ", sep="")

p_data %>% select(
                c('Name', 'discount', 'Quantity', 'Special.Price', 'SKU')
                ) %>%
  arrange( desc(discount) ) %>%
  View()



(p_data[p_data$discount > 0.85, ]$SKU %>% length()) / (p_data$SKU %>% length())

# p_data %>%
#   mutate(sku_stripped = substring(SKU, 5, 15) )%>%
#   select(sku_stripped) %>%
#   write_csv("data_content.csv")

