#load library titanic
library(titanic)

# Overview
head(titanic_train)
df <- titanic_train
glimpse(df)

## Drop NA missing value
nrow(df)
nrow(df) - sum(complete.cases(df)) # num of missing value row
df <- na.omit(df)

cor(df[, c("Survived", "Pclass", "Age", "SibSp", "Parch", "Fare")])

## convert Survived to factor for dependent variable, 
#df$Survived <- factor(df$Survived, 
#                   levels = c(0,1),
#                   labels = c("Died", "Survied"))
class(df$Survived)
table(df$Survived)

##  SPLIT DATA
set.seed(42)
n <- nrow(df)
id <- sample(1:n, size = n*0.7) 
train_data <- df[id, ]
test_data <- df[-id, ]

## Logistic Regression for predict factor 2 values[0-1] = binary classification
# survived = fn(Pclass)
logit_model <- glm(Survived ~ Pclass + Age + Fare, data = train_data, family= "binomial")
#summary(logit_model)

## Train Model use rogistic regression
p_train <- predict(logit_model, type="response")  # probability 0-1
train_data$pred <- if_else(p_train >= 0.5, "1", "0")
train_data$Survived == train_data$pred
mean(train_data$Survived == train_data$pred)  # accuracy

## Test Model
p_test <- predict(logit_model, newdata = test_data, type="response")
test_data$pred <- if_else(p_test >= 0.5, "1", "0")
test_data$Survived == test_data$pred
mean(test_data$Survived == test_data$pred)

## confusion matrix
# four factor - table
conM <- table(test_data$pred, test_data$Survived, dnn = c("Predicted", "Actual"))
cat("Accuracy:",(conM[1,1] + conM[2,2])/sum(conM))
cat("Precision:",conM[2,2]/sum(conM[2,]))
cat("Recall:",conM[2,2]/sum(conM[,2]))
cat("F1:",2*((0.9*0.9)/(0.9+0.9)))

