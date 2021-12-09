# create public subnet
resource "aws_subnet" "controller_subnet" {
	vpc_id = aws_vpc.main.id
	cidr_block = "74.11.3.0/24"
	map_public_ip_on_launch = true
	tags = {
		Name = "eng74-fp-controller_subnet"
	}
}
# configuring route table association
resource "aws_route_table_association" "controller_subnet_assoc"{
	subnet_id = aws_subnet.controller_subnet.id
	route_table_id = aws_route_table.public_rt.id
}

# create NACL for controller subnet
resource "aws_network_acl" "controller_nacl" {
	vpc_id = aws_vpc.main.id
	subnet_ids = [aws_subnet.controller_subnet.id]

	# allow HTTP from all
	ingress {
		protocol = "tcp"
		rule_no = 100
		action = "allow"
		cidr_block = "0.0.0.0/0"
		from_port = 80
		to_port = 80
	}

	# allow HTTPS from all
	ingress {
		protocol = "tcp"
		rule_no = 110
		action = "allow"
		cidr_block = "0.0.0.0/0"
		from_port = 443
		to_port = 443
	}

	# allow SSH from home
	ingress {
		protocol = "tcp"
		rule_no = 120
		action = "allow"
		cidr_block = "${var.my_ip}/32"
		from_port = 22
		to_port = 22
	}

	# allow ephemeral from all
	ingress {
		protocol = "tcp"
		rule_no = 130
		action = "allow"
		cidr_block = "0.0.0.0/0"
		from_port = 1024
		to_port = 65535
	}

	# allow SSH for extra user
	ingress {
		protocol = "tcp"
		rule_no = 140
		action = "allow"
		cidr_block = "${var.extra_user_ip}/32"
		from_port = 22
		to_port = 22
	}

	# allow SSH from public subnet
	ingress {
		protocol = "tcp"
		rule_no = 150
		action = "allow"
		cidr_block = "74.11.1.0/24"
		from_port = 22
		to_port = 22
	}
	
	# allow HTTP to all
	egress {
		protocol = "tcp"
		rule_no = 100
		action = "allow"
		cidr_block = "0.0.0.0/0"
		from_port = 80
		to_port = 80
	}

	# allow HTTPS to all
	egress {
		protocol = "tcp"
		rule_no = 110
		action = "allow"
		cidr_block = "0.0.0.0/0"
		from_port = 443
		to_port = 443
	}

	# allow SSH to home
	egress {
		protocol = "tcp"
		rule_no = 120
		action = "allow"
		cidr_block = "${var.my_ip}/32"
		from_port = 22
		to_port = 22
	}

	# allow ephemeral to all
	egress {
		protocol = "tcp"
		rule_no = 130
		action = "allow"
		cidr_block = "0.0.0.0/0"
		from_port = 1024
		to_port = 65535
	}

	# allow 27017 to private subnet
	egress {
		protocol = "tcp"
		rule_no = 140
		action = "allow"
		cidr_block = "74.11.2.0/24"
		from_port = 27017
		to_port = 27017
	}

	# allow SSH to matt
	egress {
		protocol = "tcp"
		rule_no = 150
		action = "allow"
		cidr_block = "${var.extra_user_ip}/32"
		from_port = 22
		to_port = 22
	}

	# allow SSH to public subnet
	egress {
		protocol = "tcp"
		rule_no = 160
		action = "allow"
		cidr_block = "74.11.1.0/24"
		from_port = 22
		to_port = 22
	}

	# allow SSH out to everyone in order to connect to github
	egress {
		protocol = "tcp"
		rule_no = 170
		action = "allow"
		cidr_block = "0.0.0.0/0"
		from_port = 22
		to_port = 22
	}

	

	tags = {
		Name = "eng74-fp-controller_nacl"
	}
}