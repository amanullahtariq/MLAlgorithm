setwd("D:/repo/github/MachineLearning/Custom/Titanic")
titanic.train <- read.csv(file =  "train.csv",stringsAsFactors = FALSE, header = TRUE)
titanic.test <- read.csv(file =  "test.csv",stringsAsFactors = FALSE, header = TRUE)

# mark train and test set and combine
titanic.train$IsTrainSet <- TRUE
titanic.test$IsTrainSet <- FALSE


# Add Survived column so test and train both have same column 
# so we can combine them
titanic.test$Survived <- NA


titanic.full <- rbind(titanic.train, titanic.test)
titanic.full[titanic.full$Embarked == '', "Embarked"] <- 'S'

#replace missing age with meadian
age.median <- median(titanic.full$Age, na.rm = TRUE) 

titanic.full[is.na(titanic.full$Age), "Age"] <- age.median

#clean missing value of fare
fare.median <- median(titanic.full$Fare, na.rm = TRUE) 
titanic.full[is.na(titanic.full$Fare), "Fare"] <- fare.median

# categorical casting except of survived 
titanic.full$Pclass <- as.factor(titanic.full$Pclass)
titanic.full$Sex <- as.factor(titanic.full$Sex)
titanic.full$Embarked <- as.factor(titanic.full$Embarked)


# Split dataset back into to train and test
titanic.train <- titanic.full[titanic.full$IsTrainSet == TRUE,]
titanic.test <- titanic.full[titanic.full$IsTrainSet == FALSE,]

titanic.train$Survived <- as.factor(titanic.train$Survived)


survived.equation <- "Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked"
survived.formula <- as.formula(survived.equation)

install.packages("randomForest")
library(randomForest)

titanic.model <- randomForest(formula = survived.formula, data = titanic.train, ntree = 500 , mtry = 3, nodesize = 0.01 * nrow(titanic.train))

features.equation <- "Pclass + Sex + Age + SibSp + Parch + Fare + Embarked"

Survived <- predict(titanic.model, titanic.test)

PassengerId <- titanic.test$PassengerId
output.df <- as.data.frame(PassengerId)
output.df$Survived <- Survived

write.csv(output.df,file = "kaggle_submission.csv", row.names = FALSE)

