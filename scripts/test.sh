#! /bin/bash
echo "Testing session"

cd service1
echo "installing requirements for service 1"
pip3 install -q -r requirements.txt
echo "requirements done!"
echo ""
echo "Testing Service 1..."
python3 -m pytest --cov application --cov-report term-missing
echo "Test for service 1 complete!"
cd ..

cd service2
echo "installing requirements for service 2"
pip3 install -q -r requirements.txt
echo "requirements done!"
echo ""
echo "Testing Service 2..."
python3 -m pytest --cov application --cov-report term-missing
echo "Test for service 2 complete!"
cd ..

cd service3
echo "installing requirements for service 3"
pip3 install -q -r requirements.txt
echo "requirements done!"
echo ""
echo "Testing Service 3..."
python3 -m pytest --cov application --cov-report term-missing
echo "Test for service 3 complete!"
cd ..

cd service4
echo "installing requirements for service 4"
pip3 install -q -r requirements.txt
echo "requirements done!"
echo ""
echo "Testing Service 4..."
python3 -m pytest --cov application --cov-report term-missing
echo "Test for service 4 complete!"
cd ..
