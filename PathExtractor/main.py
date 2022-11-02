import json
import os

from datasetprocess.CodeApiExtractor import CodeApiExtractor
from datasetprocess.CodeBagOfWordExtractor import CodeBagOfWordExtractor
from datasetprocess.CodeCfgPathsExtractor import CodeCfgPathsExtractor
from datasetprocess.DocStringExtractor import DocStringExtractor
from datasetprocess.FuncNameExtractor import FuncNameExtractor


def process_cfg(input_file, output_file, need_method_name):
    file_input = open(input_file, 'r', encoding='utf-8')
    file_output = open(output_file, 'w', encoding='utf-8')
    id_num = 0
    for line in file_input.readlines():
        id_num += 1
        print(id_num)
        code = line.strip()
        cfg_path = CodeCfgPathsExtractor.extract(code, need_method_name)

        file_output.write(json.dumps(cfg_path) + '\n')


if __name__ == '__main__':
    # code = '''
    # public int FindProc(String id){
    #     int i=0;
    #     while(i<procs.size()){
    #         ProcedureEntry pe=procs.elementAt(i);
    #         if(pe.name.equals(id)){
    #             return i1;}
    #         i=i+1;}
    #     return i2;}
    # '''
    # code1='''
    # private void mapAbsoluteToRelative ( float [ ] destPoints , float [ ] srcPoints , int numPoints ) { for ( int i = NUM_ ; i < numPoints ; i ++ ) { destPoints [ i * NUM_ + NUM_ ] = ( srcPoints [ i * NUM_ + NUM_ ] - mImageBounds . left ) / mImageBounds . width ( ) ; destPoints [ i * NUM_ + NUM_ ] = ( srcPoints [ i * NUM_ + NUM_ ] - mImageBounds . top ) / mImageBounds . height ( ) ; } }
    #
    # '''
    # # 1,2,3,4,5,7
    # # 1,2,3,4,5
    # # 1,2,3,4,5,6
    # cfg_path = CodeCfgPathsExtractor.extract(code1, True)
    # for item in cfg_path:
    #     print(item)
    #
    #
    # print(json.dumps(cfg_path) + '\n')
    need_method_name = True # 是否需要方法名
    # dir = 'D:\\code\\data_RQ1'
    dir = '/headless/qhj/ATCP/data_set/processed/java'
    # dir = 'D:\\000准备毕设\\transfomer对应的数据集\\data\\java'
    data_set = ['train', 'dev', 'test']
    #data_set = ['dev', 'test']
    for item in data_set:
        input_dir = os.path.join(dir, item, 'code_unsubtoken.seq')
        #input_dir = os.path.join(dir, item, 'code.original')
        output_dir = os.path.join(dir, item, 'cfg_unsplit.seq')
        #output_dir = os.path.join(dir, item, item+'.token.path')
        process_cfg(input_dir, output_dir, need_method_name)


    # process_cfg('/headless/qhj/ATCP/data_set/processed/java/dev/code_unsubtoken.seq',
    #             '/headless/qhj/ATCP/data_set/processed/java/dev/cfg_unsplit.seq', need_method_name)