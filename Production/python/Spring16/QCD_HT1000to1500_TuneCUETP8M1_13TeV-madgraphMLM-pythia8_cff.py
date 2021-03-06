import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/004BCBAD-BE03-E611-A4AD-90B11C08CDB7.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/0A108DB2-7D04-E611-9B4E-0025905A609E.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/1650EF77-0603-E611-8A1B-003048FFCBB2.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/1AD7DFE4-A903-E611-A92A-C81F66B7F2C9.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/26F74641-3303-E611-9EDE-0CC47A4D768E.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/4C188AF5-6703-E611-A76D-842B2B17F557.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/5CD90E48-0603-E611-B539-0CC47A78A4BA.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/5E9B8F83-4403-E611-AA76-0025905A612A.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/6C2DBF23-3E03-E611-B92B-003048FFD7AA.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/8C329748-6703-E611-8959-1418774121A1.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/8C931DED-B203-E611-9A2D-0025905A60FE.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/902D3150-9E03-E611-9EDC-842B2B185C54.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/94234EBC-9D03-E611-B933-549F3525BF58.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/987C2DA2-7603-E611-B693-008CFA1111E0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/9C3FABE2-4103-E611-8D3E-0CC47A4D768E.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/A2DCA6CB-A503-E611-B7FB-0025905A60FE.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/A8DB58D3-BE03-E611-8102-0025901FB100.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/ACF5EB83-4403-E611-9C71-0025905A60B6.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/B0C3A202-BF03-E611-BFBA-003048F5B2F0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/C40273D5-BE03-E611-B9A6-24BE05CE2E81.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/CA253ACA-9D03-E611-AC6A-B083FED4263D.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/D036C997-5203-E611-97C4-0CC47A4C8EA8.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/D6F3B3BB-FD03-E611-9628-0CC47A4D766C.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/FCE91103-3303-E611-973E-0025905A48FC.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/FEEF5ADB-2C03-E611-830F-001E67A4069F.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/003F4E4A-BE04-E611-B352-002590D9D8C2.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/0A1223AC-CE03-E611-BBA7-001E673985E3.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/10DC0574-9503-E611-8506-0CC47A78A496.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/12B9B645-2404-E611-AF93-44A842CFC9D9.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/16576D1E-2504-E611-A6FE-44A842CF0571.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/184393D2-7B03-E611-8DA3-001517FB1944.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/18F3C9E7-9303-E611-829D-001E67DFF735.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1C3048D6-B803-E611-9FBB-008CFA111330.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1CADA5D4-7B03-E611-957A-001E67A3F3DF.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1E3F2BC5-7B03-E611-BDA5-5065F37D4131.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1EA9EB1B-FA03-E611-B7CB-141877411E9A.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/28632846-2404-E611-9E41-44A842CFD5F2.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/28F68BCA-2604-E611-9572-008CFA1C6414.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/303BFE86-CE03-E611-99F9-1C6A7A26D485.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/325894DF-9303-E611-AC9D-001517FAD934.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/32EF7305-CF03-E611-8D01-0025905B861C.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/38CFB8E9-2304-E611-9D26-44A842CFD5D8.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/3A2D781E-2504-E611-ACAA-44A842CF05B2.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/3E0553EB-2304-E611-B816-44A842CF0571.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/40D2414F-DA03-E611-90ED-14187741136B.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/504B2887-CE03-E611-9FDA-14187741121F.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/5063D656-B004-E611-BC1D-90B11C2C93C9.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/50CF97AA-A803-E611-B819-0CC47AB0B704.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/545B1309-DA03-E611-9EC5-B083FECF83AB.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/56B8CFC2-B903-E611-BE5F-001E675A68C4.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/589D3070-8303-E611-9567-0025905A6056.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/62D9E8A1-A803-E611-BDB3-008CFA1112C0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/6498B0A0-A803-E611-BDD7-0CC47A0AD6C4.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/64CA1B9E-8103-E611-903C-90B11C06DD39.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/6C7DEED4-7B03-E611-AAA1-90B11C06DD39.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/6C92032A-CF03-E611-BCFC-008CFA1979D4.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/6CFF3275-8303-E611-8EB3-0025905A60E4.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/767D97CB-8F04-E611-80D1-6C3BE5B5A038.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/76D61479-9403-E611-8FA0-0025907D2430.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/7C38F59B-A004-E611-97CE-001E67D8A423.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/7C58D07B-9403-E611-BA09-0CC47A57CC42.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/86D32CD7-2404-E611-B4D4-0002C94D54FA.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/940679D9-B803-E611-BE5C-008CFA1113B0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/94FDC01E-2504-E611-8C20-44A842CFD5D8.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/96AE15EB-2304-E611-B923-44A842CF05B2.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/9C480782-CE03-E611-BC45-1418774120C3.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/9E32A7F4-9303-E611-9AA4-A4BADB22B414.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A05752F1-2304-E611-8A27-44A842CFD5CB.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A2541DD5-7B03-E611-AC41-90B11C06DD39.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A2B6A707-2504-E611-9985-44A842CF0571.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A2F14E79-9503-E611-A588-0CC47A4C8E70.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A8D72A96-CE03-E611-B9C7-B083FED179D6.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A8F5DBF0-8103-E611-BC2E-008CFA0A5818.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/AEDBE4ED-7B03-E611-9B19-90B11C12E856.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/B26851D2-7B03-E611-8B0A-001E675A5262.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/BE9E641E-2504-E611-BF27-44A842CFD5CB.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/BEEAE89D-A803-E611-A83E-00259055055E.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/C4CCC69D-CE03-E611-81C1-549F35AD8C17.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/C84268CB-7B03-E611-8E21-24BE05C68681.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/D00C4E28-2504-E611-83E7-6C3BE5B58058.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/DE4FEFAD-A303-E611-AF74-0025905A60FE.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/E000BAC2-2404-E611-AC3F-44A842CFD5F2.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/E20BB8F4-2304-E611-B010-6C3BE5B5A038.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/F0C15CF0-2304-E611-9EDF-44A842CFD5CB.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/F6CE43EC-2304-E611-AB8B-44A842CF0571.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/F8DA47A5-8103-E611-A781-001E675A69DC.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/FAC637ED-2304-E611-B7C6-44A842CFD5CB.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/FAF3BA0C-8203-E611-B2CF-000F530E47AC.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/02153377-BC03-E611-8B9C-0025905AA9CC.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/0C0422A5-8303-E611-A47F-0025905AA9CC.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/1207018F-9D03-E611-B8ED-001E67DDC88A.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/125EE1F3-BA03-E611-8322-1C6A7A21A73B.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/14B08069-9303-E611-BF9B-0025905B856E.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/1CB1C70F-BB03-E611-9C31-549F35AD8C24.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/2409BF52-9E03-E611-BBF0-0025904A8EC8.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/32096E69-9303-E611-BB64-0CC47A4D7616.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/38615BED-B903-E611-B1ED-00304867FD5F.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/4486086C-BC03-E611-8A37-0025905B855A.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/584ADE0E-9E03-E611-8F85-549F35AD8BF0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/5EC600FE-B903-E611-8ED4-0CC47A57CEB4.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/6448114E-8103-E611-8A46-000F5327372C.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/6A163266-1404-E611-822A-44A842CFC9D9.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/6C586080-1404-E611-A86F-0002C94CD9AA.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/6ECD1F6C-9303-E611-838D-0025905A60FE.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7494673B-D203-E611-8974-782BCB20F910.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7604566A-9303-E611-8311-0025905A48D8.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7685136E-8303-E611-9356-003048FFD7AA.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/7C9A12A5-8703-E611-BB54-0025905A609E.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/88E6B364-1404-E611-8470-44A842CFD5D8.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/8A71D3A4-8703-E611-9341-0025905B8568.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/90C49E27-8103-E611-A747-001E67A3F3DF.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/9C53E750-1404-E611-BA56-0025900EAB2A.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A20E1812-9E03-E611-9162-00266CF3DF14.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A28FA26B-9303-E611-94EC-0CC47A4C8E1C.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A4070C94-B903-E611-9BA9-008CFA1113A0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A6952F42-9E03-E611-9309-1C6A7A266B8F.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A6BEC8E1-D203-E611-93D2-5C260AFC8D10.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/AC5A7BA1-8703-E611-A20E-0025905A607E.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/B0806C4A-8703-E611-B426-549F35AF44F0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/B284175D-9603-E611-A903-549F358EB77C.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/B2D224C9-BA03-E611-8885-00266CFBE88C.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/C0DA670F-9E03-E611-9B7B-549F35AC7E70.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/C27C6BD7-E203-E611-BF87-002590A80E08.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/CC4E6F15-BB03-E611-8A9D-008CFA0A5684.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/D4B9C7FB-8603-E611-B6E0-00266CFCC21C.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/D66C6E6C-8303-E611-9EAD-0025905B860E.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/D6D144C6-9D03-E611-A4ED-549F35AF447B.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/D6D602A1-8703-E611-99FA-0025905B857C.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E007140D-BB03-E611-BB1C-549F35AE4FE3.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E0E24556-1404-E611-860A-0CC47A0AD6FE.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E2525841-D203-E611-978F-00266CFCC364.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E265766A-9603-E611-BD2B-00266CF3DFE0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E49043FB-BA03-E611-9770-001E675A68C4.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E6317227-8103-E611-8793-001E67DDCC81.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/EA0574BF-B903-E611-8911-008CFA1112C0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/EC323268-8303-E611-8E10-0CC47A4D763C.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/EC5D9C1D-BB03-E611-8654-001E67A3F70E.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/F236B16B-8303-E611-A672-0025905A60E0.root',
       '/store/mc/RunIISpring16MiniAODv1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/FCCCD8DB-D203-E611-B01F-008CFA166000.root',
] )
