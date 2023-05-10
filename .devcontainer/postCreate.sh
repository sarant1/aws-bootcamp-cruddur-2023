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

sudo npm install aws-cdk -g

echo $(pwd)
/workspaces/aws-bootcamp-cruddur-2023/bin/frontend/generate-env
/workspaces/aws-bootcamp-cruddur-2023/bin/backend/generate-env



# Install Cfn-lint
pip install cfn-lint

# Install cfn toml
chown -R bootcamp:bootcamp /var/lib/gems/3.0.0
gem install cfn-toml

# Set path to include cfn-lint
export PATH=$PATH:/home/bootcamp/.local/bin

cp /workspaces/aws-bootcamp-cruddur-2023/thumbing-serverless-cdk/.env.example /workspaces/aws-bootcamp-cruddur-2023/thumbing-serverless-cdk/.env
