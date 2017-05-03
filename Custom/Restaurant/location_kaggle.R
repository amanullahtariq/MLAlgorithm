#Getting started with Kaggle
setwd('D:/repo/github/MachineLearning/Custom/Restaurant/input/')

#Read in the training and test data
basedata <- read.csv("train.csv")
str(basedata)
basedata$Open.Date <- as.Date(basedata$Open.Date, '%m/%d/%Y')
str(basedata)
basedata$OpenDays <- as.integer(as.Date('01/01/2015', '%m/%d/%Y') - basedata$Open.Date)


testdata <- read.csv("test.csv")
testdata$Open.Date <- as.Date(testdata$Open.Date, '%m/%d/%Y')
testdata$OpenDays <- as.integer(as.Date('01/01/2015', '%m/%d/%Y') - testdata$Open.Date)



library(ggplot2)
ggplot(basedata) + aes(revenue) + geom_bar(binwidth = 150000)
ggplot(basedata) + aes(log(revenue)) + geom_bar(binwidth = 0.05)
ggplot(basedata) + aes(revenue, OpenDays) + geom_point()
ggplot(basedata) + aes(OpenDays) + geom_bar(binwidth = 200)
ggplot(basedata) + aes(log(revenue), log(OpenDays)) + geom_point()

# Model Number 1 - Revenue ~ OpenDays
lm.SimpleOpenDays = lm(log(revenue) ~ log(OpenDays), basedata)
summary(lm.SimpleOpenDays)
pred.SimpleOpenDays = predict(lm.SimpleOpenDays, data=basedata)
RMSE.SimpleOpenDays = sqrt(mean((basedata$revenue - exp(pred.SimpleOpenDays))^2))
pred.SimpleOpenDays.test = predict(lm.SimpleOpenDays, newdata=testdata)

submit<-cbind(testdata[,1],exp(pred.SimpleOpenDays.test))
colnames(submit)<-c("Id", "Prediction")
write.csv(submit, "submission_SimpleOpenDays.csv", row.names = FALSE, quote = FALSE)


# Model Number 2
ggplot(basedata) + aes(log(revenue), log(OpenDays), color=City.Group) + geom_point()
ggplot(basedata) + aes(log(revenue), log(OpenDays), color=Type) + geom_point()


