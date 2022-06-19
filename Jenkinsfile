node{
    properties([pipelineTriggers([pollSCM('* * * * *')])])
    stage("clone"){
        git branch: 'main', url: 'https://github.com/noampaz-beep/DevOps1004.git'
    }
    stage("show files"){
        bat "dir"
    }
}
