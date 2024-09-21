import subprocess
import os
import shutil


makerPath = os.path.abspath('phira-render')
resourceDir = os.path.abspath('Phigros_Resource')
PhiraDir = os.path.join(resourceDir, "phira")

processes = []
for difficulty in os.listdir(PhiraDir):
	if difficulty == 'AT':
		difficultyDir = os.path.join(PhiraDir, difficulty)
		for chartName in os.listdir(difficultyDir):
			if chartName.endswith('-rpe.pez'):
				print(chartName)
				chartPath = os.path.join(difficultyDir, chartName)
				makerdir = difficultyDir + '\\' + chartName
				os.mkdir(makerdir)
				shutil.copytree(makerPath, makerdir)
				maker = os.path.join(os.path.join(makerdir, 'phira-render'), 'phira-render.exe')
				processes.append(
					subprocess.Popen(
						[maker, chartPath]
					)
				)
for p in processes:
	p.wait()