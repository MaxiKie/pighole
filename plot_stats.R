library(dplyr)
library(ggplot2)
dat=read.csv('/home/maxi/pighole/stats.csv',sep=';')
colnames(dat)=c('wins','strat')
dat=data.frame(strat=dat$strat,wins=dat$wins)
plot(dat)
dat1 = dat %>% mutate(bin = ntile(strat, n=100))
dat2 = dat1 %>% group_by(bin) %>% summarise(stratmean = mean(strat), winmean = mean(wins)) #find the x and y mean of each bin

ggplot(dat,aes(x=strat,y=wins))+geom_point()+geom_smooth()
ggplot(dat,aes(x=strat,y=wins))+geom_bin_2d(bins=50)

ggplot(dat2, aes(x=stratmean, y=winmean)) + geom_point() + geom_smooth()
