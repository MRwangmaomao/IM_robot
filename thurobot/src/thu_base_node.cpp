#include <ros/ros.h>
#include "thu_base.h"

int main(int argc, char** argv )
{
    ros::init(argc, argv, "thu_base_node");
    RikiBase thu;
    sleep(6);
    std::cout <<std::endl;
    std::cout <<std::endl;
    std::cout <<std::endl;
     std::cout <<std::endl; 
    std::cout << "                #################################################" << std::endl;
    std::cout << "                #################################################" << std::endl;
    std::cout << "                ####         ##### ######## ##### ######## ######" << std::endl;
    std::cout << "                ######## ######### ######## ##### ######## ######" << std::endl;
    std::cout << "                ######## ######### ######## ##### ######## ######" << std::endl;
    std::cout << "                ######## ######### ######## ##### ######## ######" << std::endl;
    std::cout << "                ######## #########          ##### ######## ######" << std::endl;
    std::cout << "                ######## ######### ######## ##### ######## ######" << std::endl;
    std::cout << "                ######## ######### ######## ##### ######## ######" << std::endl;
    std::cout << "                ######## ######### ######## ##### ######## ######" << std::endl;
    std::cout << "                ######## ######### ######## #####          ######" << std::endl;
    std::cout << "                #################################################" << std::endl;
    std::cout << "                #################################################" << std::endl; 
    std::cout <<std::endl;
    std::cout <<std::endl;
    std::cout << "                   欢迎使用清华大学先进制造学部智能制造机器人平台" << std::endl;
    std::cout <<std::endl;
    std::cout <<std::endl;
    std::cout <<std::endl;
    std::cout <<std::endl;
    ros::spin();
    return 0;
}
