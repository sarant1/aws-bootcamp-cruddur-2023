#! /usr/bin/bash

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="rds-update-sg-rule"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"

export CURRENT_IP=$(curl ifconfig.me)

aws ec2 modify-security-group-rules --group-id $DB_SG_ID --security-group-rules "SecurityGroupRuleId=$DB_SG_RULE_ID,SecurityGroupRule={IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$CURRENT_IP/32,Description="GITPOD"}"
curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb" -o "session-manager-plugin.deb"
sudo dpkg -i session-manager-plugin.deb

rm session-manager-plugin.deb

echo $(pwd)
./bin/frontend/generate-env
./bin/backend/generate-env
