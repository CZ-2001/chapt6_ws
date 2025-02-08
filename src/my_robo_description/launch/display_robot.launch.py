import launch
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory
import launch_ros.parameter_descriptions

def gener_laun_des():
    #获取默认的urdf的路径 
    urdf_pack_path=get_package_share_directory('my_robo_description')
    defa_urdf_path=os.path.join(urdf_pack_path,'URDF','my_robo.urdf')
    #声明一个urdf参数方便修改
    action_declare_arg_mode_path=launch.actions.DeclareLaunchArgument(
        name='model',default_value=str(defa_urdf_path),description='加载的模型文件路径'
    )
    #通过文件路径，获取内容  ，并转变成参数值对象 ，以供传入   robot_state_publisher  
    sub_command_result=launch.substitutions.Command('cat',launch.substitutions.LaunchConfiguration
                                 ('model'))
    rob_describle_value=launch_ros.parameter_descriptions.ParameterValue(sub_command_result,value_type=str)
    
                                                                                                                                                                                                                                                                                                                                          
    action_rob_state_pub=launch_ros.actions.Node(
        package='robot_state_publisher',
        exec_name='robot_state_publisher',
        parameters=[{'robot_description':rob_describle_value}]
    )
                                                                                                                                                                                                                                                                                                                                          
    action_joint_state_pub=launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
    )
    action_rviz2_node=launch_ros.actions.Node(
        package='rviz2',
        exec_name='rviz2'
    )
    
    
    
    return launch.LaunchDescription([
        action_declare_arg_mode_path,
        action_rob_state_pub,
        action_joint_state_pub,           
                                     ])



