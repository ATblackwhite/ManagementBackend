# ManagementBackend
软件工程大作业
后台管理子系统组
组员：林浩翰 陈韬营 董梦凡 崔浩辰 邹家轩 武云
目标用户功能：
1）用户管理：管理后台管理子系统用户、掌上博物馆用户、知识服务子系统用户的基础信息。如：对用户信息的增删查改功能；用户权限的管理，如登录、点赞、评论等用户功能的管理。例如，如果掌上博物馆用户发表不良评论，则停止其发表评论的权限。
2）信息审核：审核用户发表的留言、图片、音视频等内容的功能。对于审核不通过的内容会被屏蔽，同时对该用户进行一定程度惩罚，如禁止发评论等。自动审核功能：对于留言，可以设置敏感词，当用户提交留言出现敏感词时，进行自动屏蔽；对于图片，需要判断是否为不良图片，如果审核不通过，则不显示。人工审核功能：后台管理员或审核人员人工检查用户提交的文本、图片、音视频。
3）数据管理：管理1-3中涉及的所有数据，对所有数据可以进行增删改查等操作，支持单个操作和批量操作。
4）数据备份和恢复：支持数据库的备份和恢复。实现手动备份恢复或定时备份功能。支持查看所有的备份和恢复记录，显示记录时间等相关功能。可通过点击备份记录来将数据库恢复到该备份记录点上。
5）日志管理：查看和检索后台管理子系统的操作日志。记录包括管理员等用户对后台数据的操作记录，数据库的备份还原等记录。
