import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",
                     fileNames = readFiles, 
                     secondaryFileNames = secFiles,
                     duplicateCheckMode = cms.untracked.string("noDuplicateCheck")
                     )
readFiles.extend( [
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00000/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00001/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00002/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00003/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00004/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00005/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00006/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00007/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00008/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00009/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00010/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00011/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00012/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00013/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00014/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00015/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00016/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00017/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00018/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00019/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00020/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00021/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00022/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00023/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00024/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00025/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00026/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00027/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00028/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00029/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00030/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00031/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00032/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00033/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00034/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00035/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00036/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00037/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00038/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00039/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00040/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00041/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00042/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00043/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00044/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00045/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00046/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00047/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00048/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00049/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00050/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00051/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00052/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00053/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00054/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00055/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00056/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00057/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00058/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00059/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00060/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00061/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00062/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00063/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00064/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00065/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00066/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00067/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00068/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00069/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00070/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00071/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00072/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00073/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00074/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00075/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00076/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00077/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00078/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00079/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00080/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00081/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00082/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00083/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00084/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00085/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00086/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00087/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00088/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00089/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00090/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00091/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00092/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00093/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00094/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00095/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00096/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00097/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00098/evts_8aod.root",
        "/store/user/bschneid/analysis/signal/TChiWZ_500_0/c2235017/p00099/evts_8aod.root"
        ])